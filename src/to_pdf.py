#from create_table_fpdf2 import PDF as PDFtable
import iofunctions
from fpdf import FPDF
from datetime import datetime, timezone, timedelta
import math


boat= {
    "name": "Inua",
    "callsign": "LJ9788",
    "mmsi": 257074950,
    "loa": 13.4,
    "hight": 18.0,
    "beam": 4.0,
    "draft": 2.0
}

showkeys =[
    "log",
    "enginehours",
    "sog",
    "cog",
    "heading",
    "stw",
    "tws",
    "twd",
    "airtemperature",
    #"airpressure",
    #"humidity",
    #"text"
    ]

headers = ["Time", "Position"] + showkeys

k_to_h = {
        "Time": "Time",
        "Position": "Position",
        "log": "Log",
        "enginehours": "Engine",
        "cog": "COG",
        "sog": "SOG",
        "stw": "STW",
        "heading": "Hdg",
        "airpressure": "Baro",
        "airtemperature": "temp.",
        "twd": "TWD",
        "tws": "TWS",
        "humidity": "Humidity",
        "text": "Text",
        "fixtype": "Fix",
        "hdop": "HDOP(m)",
        "visibility": "Vis.",
        "cloudcover": "Cloud(8th)",
        "seastate": "Sea",
        "crewNames": "Crew",
        "place": "Place",
}  

# qplog = iofunctions.getQPlog("/Users/enno/Documents/dev/QPlogbook/log/2024-08.json")
# qplog = iofunctions.splitdayly(qplog)

def mk_table(log, conf, keys_to_head):
    keys = ["Time", "Position"] + conf["showkeys"]
    data = []
    header = []
    text = ""
    for key in keys:    
        header.append(keys_to_head[key])
    data.append(header)
    for entry in log:
        row = []
        for key in keys:
            if key == "Time":
                displaytime = entry["point"].time.astimezone(timezone(timedelta(hours=conf["utc_offset"])))
                row.append(displaytime.strftime('%H:%M'))
            elif key == "Position":
                pos = entry["point"].getDMpos()
                row.append(pos[0] + " " + pos[1])
            elif key in entry:
                row.append(entry[key])
            else:
                row.append("")
        data.append(row)
    for entry in log:
        if "text" in entry:
            text = text + entry["text"] + "\n"
    return (data, text)




class PDFtable(FPDF):
    def create_table(self, table_data, text_data="", title='', tz='', data_size = 10, title_size=12, align_data='L', align_header='L', x_start='x_default',emphasize_data=[], emphasize_style=None,emphasize_color=(0,0,0)): 
        """
        table_data: 
                    list of lists with first element being list of headers
        text_data:
                    text to be added below
        tz:
                    timezone (subtitle) to be added on the right margin og title
        title: 
                    (Optional) title of table (optional)
        data_size: 
                    the font size of table data
        title_size: 
                    the font size fo the title of the table
        align_data: 
                    align table data
                    L = left align
                    C = center align
                    R = right align
        align_header: 
                    align table data
                    L = left align
                    C = center align
                    R = right align
        x_start: 
                    where the left edge of table should start
        emphasize_data:  
                    which data elements are to be emphasized - pass as list 
                    emphasize_style: the font style you want emphaized data to take
                    emphasize_color: emphasize color (if other than black) 
        
        """
        default_style = self.font_style
        if emphasize_style == None:
            emphasize_style = default_style





        # Get Width of Columns
        def get_col_widths():
            
            col_widths = []

            # searching through columns for largest sized cell (not rows but cols)
            for col in range(len(table_data[0])): # for every row
                longest = 0 
                for row in range(len(table_data)):
                    cell_value = str(table_data[row][col])
                    value_length = self.get_string_width(cell_value)
                    if value_length > longest:
                        longest = value_length
                col_widths.append(longest + 4) # add 4 for padding
            col_width = col_widths

            return col_width


        header = table_data[0]
        data = table_data[1:]

        line_height = self.font_size * 1.3

        col_width = get_col_widths()
        self.set_font(size=title_size)

        # Get starting position of x
        # Determin width of table to get x starting point for centred table
        if x_start == 'C':
            table_width = 0
            if isinstance(col_width, list):
                for width in col_width:
                    table_width += width
            else: # need to multiply cell width by number of cells to get table width 
                table_width = col_width * len(table_data[0])
            # Get x start by subtracting table width from pdf width and divide by 2 (margins)
            margin_width = self.w - table_width
            # TODO: Check if table_width is larger than pdf width

            center_table = margin_width / 2 # only want width of left margin not both
            x_start = center_table
            self.set_x(x_start)
        elif isinstance(x_start, int):
            self.set_x(x_start)
        elif x_start == 'x_default':
            x_start = self.set_x(self.l_margin)


        # TABLE CREATION #

        # add title
        if title != '':
            self.cell(0, line_height, title, border=0, align='L')
            #print(self.get_y())
            if tz != '':
                self.set_font(size=6)
                self.set_y(self.get_y() + 1)
                self.set_x(sum(col_width) - self.get_string_width(tz) + 8)
                self.cell(h=line_height, text=tz, border=0)
            self.ln(line_height) # move cursor back to the left margin

        # add header
        self.set_font(size=data_size)
        y1 = self.get_y()
        if x_start:
            x_left = x_start
        else:
            x_left = self.get_x()
        x_right = self.epw + x_left
        if  not isinstance(col_width, list):
            if x_start:
                self.set_x(x_start)
            for datum in header:
                self.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3, max_line_height=self.font_size)
                x_right = self.get_x()
            self.ln(line_height) # move cursor back to the left margin
            y2 = self.get_y()
            self.line(x_left,y1,x_right,y1)
            self.line(x_left,y2,x_right,y2)

            for row in data:
                if x_start: # not sure if I need this
                    self.set_x(x_start)
                for datum in row:
                    if datum in emphasize_data:
                        self.set_text_color(*emphasize_color)
                        self.set_font(style=emphasize_style)
                        self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size)
                        self.set_text_color(0,0,0)
                        self.set_font(style=default_style)
                    else:
                        self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                self.ln(line_height) # move cursor back to the left margin
        
        else:
            if x_start:
                self.set_x(x_start)
            for i in range(len(header)):
                datum = header[i]
                self.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, new_x="RIGHT", new_y="TOP", max_line_height=self.font_size)
                x_right = self.get_x()
            self.ln(line_height) # move cursor back to the left margin
            y2 = self.get_y()
            self.line(x_left,y1,x_right,y1)
            self.line(x_left,y2,x_right,y2)


            for i in range(len(data)):
                if x_start:
                    self.set_x(x_start)
                row = data[i]
                for i in range(len(row)):
                    datum = row[i]
                    if not isinstance(datum, str):
                        datum = str(datum)
                    adjusted_col_width = col_width[i]
                    if datum in emphasize_data:
                        self.set_text_color(*emphasize_color)
                        self.set_font(style=emphasize_style)
                        self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, new_x="RIGHT", new_y="TOP", max_line_height=self.font_size)
                        self.set_text_color(0,0,0)
                        self.set_font(style=default_style)
                    else:
                        self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, new_x="RIGHT", new_y="TOP", max_line_height=self.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                self.ln(line_height) # move cursor back to the left margin
        y3 = self.get_y()
        self.line(x_left,y3,x_right,y3)

        self.multi_cell(w=x_right-x_left, text=text_data, align='L')



class PDF(PDFtable):
    def header(self):
        self.set_font("Helvetica", "I", 11)
        self.cell(0, 10, f" {boat['name']}  {boat['callsign']}", 0, new_x="LMARGIN", new_y="NEXT", align='L')

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, "Page %s" % self.page_no(), align='C')



def  mk_pdf(qplog, conf, fontsize, filename):
    #headers = ["Time", "Position"] + conf["showkeys"]
    qplog = iofunctions.splitdayly(qplog)
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=fontsize)
    for day, log in qplog.items():
        title = log[0]["point"].time.strftime('%d.%m.%Y %A')
        timezone = f" TZ: UTC{math.trunc(conf['utc_offset']):+03}:{(abs(conf['utc_offset']-math.trunc(conf['utc_offset']))*60):02.0f} "
        data = mk_table(log, conf, k_to_h)

        pdf.create_table(table_data = data[0], text_data=data[1], title=title, tz=timezone, data_size=fontsize)

        pdf.ln()

    pdf.output(filename)



# testing:

if __name__=='__main__':
    import os
    import orjson
    qplog = iofunctions.getQPlog("/Users/enno/Documents/dev/QPlogbook/log/2024-08.json")
    
    conf_file = os.path.dirname(os.path.realpath(__file__)) + "/" + "data/conf.json"
    with open(conf_file, "r") as conffile:
        conf = orjson.loads(conffile.read())

    mk_pdf(qplog, conf, 8, "test.pdf")
