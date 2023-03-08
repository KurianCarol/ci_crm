from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk
from tkinter.messagebox import askyesno
import time
import tkinter as tk



def masterPage():
    import customtkinter as ctk
    import tkinter as tk
    import sqlite3
    from PIL import ImageTk, Image
    def refresh_():
        ans = askyesno(title="Warning", message='Do you want to refresh? ')
        if ans:
            root.destroy()
            masterPage()
    def exit_():
        ans = askyesno(title="Exit Warning", message='Do you want to Exit?')
        if ans:
            root.destroy()

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    root.title("Cool India")         #windows title
    root.iconbitmap("ci_logo.ico")          #title bar icon
    fwidth = root.winfo_screenwidth()
    fheight = root.winfo_screenheight()
    root.geometry(f"{fwidth}x{fheight}")
    root.attributes('-fullscreen',True)
#=====================          option frame        ==========================================



    opt_fr = tk.Frame(root, bg='#3C84AB')
    opt_fr.pack(side=tk.LEFT)
    opt_fr.pack_propagate(False)
    opt_fr.configure(height=fheight, width=200, bd=5, relief="raised")
# =====================              option frame buttons           =============================================
    h_btn = ctk.CTkButton(opt_fr, text="Home", font=("Arial", 15), width=150, height=60,
                          command=lambda: indicate(h_btn_ind, home_page))
    h_btn.place(x=10, y=150)
    h_btn_ind = tk.Label(opt_fr, text="", bg="#1e81b0")
    h_btn_ind.place(x=3, y=150, width=5, height=60)
    js_btn = ctk.CTkButton(opt_fr, text="Job Sheet", font=("Arial", 15), width=150, height=60,
                           command=lambda: indicate(js_btn_ind, js_page))
    js_btn.place(x=10, y=255)
    js_btn_ind = tk.Label(opt_fr, text="", bg="#1e81b0")
    js_btn_ind.place(x=3, y=255, width=5, height=60)
    csd_btn = ctk.CTkButton(opt_fr, text="Info", font=("Arial", 15), width=150, height=60,
                            command=lambda: indicate(csd_btn_ind, csd_page))
    csd_btn.place(x=10, y=360)
    csd_btn_ind = tk.Label(opt_fr, text="", bg="#1e81b0")
    csd_btn_ind.place(x=3, y=360, width=5, height=60)
    rtl_btn = ctk.CTkButton(opt_fr, text="Refresh", font=("Arial", 15), width=150, height=30, command=refresh_)
    rtl_btn.place(x=10, y=600)
    rtl_btn_ind = tk.Label(opt_fr, text="", bg="#1588b7")
    rtl_btn_ind.place(x=3, y=600, width=5, height=10)
    ref_btn = ctk.CTkButton(opt_fr, text="Exit", font=("Arial", 15), width=150, height=30, command=exit_)
    ref_btn.place(x=10, y=650)
    ref_btn_ind = tk.Label(opt_fr, text="", bg="#1588b7")
    ref_btn_ind.place(x=3, y=650, width=5, height=10)


#......................................................................................................................
    def req():
        conn=sqlite3.connect('database.db')
        b_cur=conn.cursor()
        b_cur.execute("SELECT brand from req where brand is not null")
        b_list=b_cur.fetchall()
        z_cur=conn.cursor()
        z_cur.execute("SELECT zone from req where zone is not null")
        z_list=z_cur.fetchall()
        m_cur=conn.cursor()
        m_cur.execute("select mechanic from req where mechanic is not null")
        m_list=m_cur.fetchall()
        h_cur=conn.cursor()
        h_cur.execute('select helper from req where helper is not null')
        h_list=h_cur.fetchall()
        a_cur=conn.cursor()
        a_cur.execute('select type from req where type is not null')
        a_list=a_cur.fetchall()
        for item in b_list:
            ac_brand_list.append(item[0])
        for item in z_list:
                zone_list.append(item[0])
        for item in m_list:
            mechanic_list.append(item[0])
        for item in h_list:
            helper_list.append(item[0])
        for item in a_list:
            ac_cap_list.append(item[0])

    mechanic_list = []
    helper_list = []
    zone_list = []
    ac_cap_list = []
    ac_brand_list = []
    req()

# ===========================================    option frame functions    =====================================================
    def hide_indicators():
        h_btn_ind.config(bg="#1e81b0")
        js_btn_ind.config(bg="#1e81b0")
        csd_btn_ind.config(bg="#1e81b0")
        rtl_btn_ind.config(bg="#1e81b0")
        ref_btn_ind.config(bg="#1e81b0")
    def indicate(lb, page):
        hide_indicators()
        lb.config(bg="navy")
        delete_pages()
        page()
# ====================================================================================================================
    def home_page():
        def search_from_jobsheet(searchKey):
            def searchjs(searchKey):
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet WHERE job_id=?",(searchKey,))
                rows = cur.fetchall()
                conn.close()
                return rows
            jobsheet_table = ttk.Treeview(f2,columns=("jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech","helper", "tin", "tout", "desc", "materials", "charge", "expense","zone"))
            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)

            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"

            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill=BOTH, expand=1)
            rowsDisplay = searchjs(searchKey)
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', iid=record[0], text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
        def all_jobsheet():
            def view_all_js():
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet")
                rows = cur.fetchall()
                rows.reverse()
                conn.close()
                return rows
            ety=ctk.CTkEntry(f2)
            ety.pack(side='bottom')
            jobsheet_table = ttk.Treeview(f2,
                                          columns=("jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                                                   "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                                   "zone"))

            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)
#.........................................................................
            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"

            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill='y', expand=1)
            rowsDisplay = view_all_js()
            count=0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', iid=record[0], text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
                count+=1
            ety.insert(0,count)
        def search_by_cust(searchKey):
            def searchcs(searchKey):
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet WHERE mobile=?", (searchKey,))
                rows = cur.fetchall()
                conn.close()
                return rows
            ety=ctk.CTkEntry(f2)
            ety.pack(side='bottom')
            jobsheet_table = ttk.Treeview(f2,
                                          columns=(
                                              "jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                                              "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                              "zone",))
            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)
#--------------------------------------------------------------------------------------------------------
            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"
#----------------------------------------------------------------------------------------------
            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill=BOTH, expand=1)
            rowsDisplay = searchcs(searchKey)
            count = 0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
                count+=1
            ety.insert(0,count)
        def search_by_emp(searchKey):
            def searchEmpM(searchKey):
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet WHERE mech=?", (searchKey,))
                rows = cur.fetchall()
                conn.close()
                return rows
            def searchEmpH(searchKey):
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet WHERE helper=?", (searchKey,))
                rows = cur.fetchall()
                conn.close()
                return rows
            ety = ctk.CTkEntry(f2, placeholder_text="entry", )
            ety.pack(side='bottom')
            jobsheet_table = ttk.Treeview(f2,
                                          columns=(
                                              "jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                                              "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                              "zone"))
            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)
#........................................................................................................................
            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"
            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill=BOTH, expand=1)
            if searchKey in mechanic_list:
                rowsDisplay = searchEmpM(searchKey)
            else:
                rowsDisplay = searchEmpH(searchKey)
            count = 0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', iid=record[0], text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
                count += 1
            ety.insert(0, count)
        def search_by_date(searchKey):
            def searchDate(searchKey):
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet WHERE date=?", (searchKey,))
                rows = cur.fetchall()
                conn.close()
                return rows
            ety = ctk.CTkEntry(f2, placeholder_text="entry", )
            ety.pack(side='bottom')
            jobsheet_table = ttk.Treeview(f2, columns=(
                "jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                "zone",))

            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            # scv.grid(row=0, column=2, rowspan=2)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            # sch.grid(row=5, column=0, columnspan=2)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)

            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"

            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)

            jobsheet_table.pack(fill=BOTH, expand=1)

            rowsDisplay = searchDate(searchKey)
            count = 0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
                count += 1
            ety.insert(0, count)
        def search_by_date_range(seachKey):
            text = seachKey
            sK = list(map(str, text.split(' ')))
            v1 = str(sK[0])
            v2 = str(sK[1])
            def searchDateRange():
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet where date between ? and ?", (v1, v2))
                rows = cur.fetchall()
                conn.close()
                return rows
            ety = ctk.CTkEntry(f2, placeholder_text="entry", )
            ety.pack(side='bottom')

            jobsheet_table = ttk.Treeview(f2,
                                          columns=(
                                              "jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                                              "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                              "zone",))
            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)
            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"

            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill=BOTH, expand=1)
            rowsDisplay = searchDateRange()
            count = 0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))

                count += 1
            ety.insert(0, count)
        def search_by_zone(searchKey):
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM JOBSHEET WHERE zone =?", (searchKey,))
            rows = cur.fetchall()
            rows.reverse()
            ety = ctk.CTkEntry(f2, placeholder_text="entry", )
            ety.pack(side='bottom')
            jobsheet_table = ttk.Treeview(f2,
                                          columns=("jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                                                   "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                                   "zone"))
            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)
            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"
            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill=BOTH, expand=1)
            rowsDisplay = rows
            count = 0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', iid=record[0], text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
                count += 1
            ety.insert(0, count)
        def search_by_zoneDate(searchKey):
            print(searchKey)
            k = searchKey.split(' ')
            if k[0] in zone_list:
                try:
                    conn = sqlite3.connect("database.db")
                    cur = conn.cursor()
                    cur.execute("select * from jobsheet where zone=? and date=?", (k[0], k[1]))
                    rows = cur.fetchall()
                    rows.reverse()
                    ety=ctk.CTkEntry(f2)
                    ety.pack(side='bottom')
                    jobsheet_table = ttk.Treeview(f2,
                                                  columns=(
                                                      "jobid", "date", "name", "mobile", "address", "brand", "Cap",
                                                      "Mech",
                                                      "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                                      "zone"))

                    scv = ctk.CTkScrollbar(f2, height=300)
                    scv.pack(side='right', fill=Y)
                    jobsheet_table.configure(yscrollcommand=scv.set)
                    scv.configure(command=jobsheet_table.yview)
                    sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
                    sch.pack(side='bottom', fill=X)
                    jobsheet_table.configure(xscrollcommand=sch.set)
                    sch.configure(command=jobsheet_table.xview)

                    jobsheet_table.heading("jobid", text="Jid")
                    jobsheet_table.heading("date", text="Date")
                    jobsheet_table.heading("name", text="Name")
                    jobsheet_table.heading("mobile", text="Mobile")
                    jobsheet_table.heading("address", text="Address")
                    jobsheet_table.heading("brand", text="brand")
                    jobsheet_table.heading("Cap", text="capacity")
                    jobsheet_table.heading("Mech", text="Mechanic")
                    jobsheet_table.heading("helper", text="Helper")
                    jobsheet_table.heading("tin", text="Time In")
                    jobsheet_table.heading("tout", text="Time Out")
                    jobsheet_table.heading("desc", text="Desc")
                    jobsheet_table.heading("materials", text="Materials")
                    jobsheet_table.heading("charge", text="Charge")
                    jobsheet_table.heading("expense", text="Expense")
                    jobsheet_table.heading("zone", text="Zone")
                    jobsheet_table["show"] = "headings"

                    jobsheet_table.column("jobid", width=40)
                    jobsheet_table.column("date", width=70)
                    jobsheet_table.column("name", width=100)
                    jobsheet_table.column("mobile", width=100)
                    jobsheet_table.column("address", width=100)
                    jobsheet_table.column("brand", width=100)
                    jobsheet_table.column("Cap", width=100)
                    jobsheet_table.column("Mech", width=100)
                    jobsheet_table.column("helper", width=100)
                    jobsheet_table.column("tin", width=100)
                    jobsheet_table.column("tout", width=100)
                    jobsheet_table.column("desc", width=100)
                    jobsheet_table.column("materials", width=100)
                    jobsheet_table.column("charge", width=100)
                    jobsheet_table.column("expense", width=100)
                    jobsheet_table.column("zone", width=100)

                    jobsheet_table.pack(fill=BOTH, expand=1)

                    rowsDisplay = rows
                    count=0
                    for record in rowsDisplay:
                        jobsheet_table.insert("", 'end', iid=record[0], text=record[0],
                                              values=(record[0], record[1], record[2], record[3], record[4],
                                                      record[5], record[6], record[7], record[8],
                                                      record[9], record[10], record[11], record[12],
                                                      record[13], record[14], record[15]))
                        count+=1
                    ety.insert(0,count)
                except:
                    print("error")
            else:
                print("error")
        def search_by_zoneDateRange(searchKey):
            text = searchKey
            sK = list(map(str, text.split(' ')))
            z = str(sK[0])
            d1 = str(sK[1])
            d2 = str(sK[2])
            def searchDateRange():
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM jobsheet where zone=? and date between ? and ?", (z, d1, d2))
                rows = cur.fetchall()
                conn.close()
                return rows
            ety = ctk.CTkEntry(f2, placeholder_text="entry", )
            ety.pack(side='bottom')
            jobsheet_table = ttk.Treeview(f2,
                                          columns=(
                                              "jobid", "date", "name", "mobile", "address", "brand", "Cap", "Mech",
                                              "helper", "tin", "tout", "desc", "materials", "charge", "expense",
                                              "zone",))
            scv = ctk.CTkScrollbar(f2, height=300)
            scv.pack(side='right', fill=Y)
            jobsheet_table.configure(yscrollcommand=scv.set)
            scv.configure(command=jobsheet_table.yview)
            sch = ctk.CTkScrollbar(f2, orientation='horizontal', width=480)
            sch.pack(side='bottom', fill=X)
            jobsheet_table.configure(xscrollcommand=sch.set)
            sch.configure(command=jobsheet_table.xview)

            jobsheet_table.heading("jobid", text="Jid")
            jobsheet_table.heading("date", text="Date")
            jobsheet_table.heading("name", text="Name")
            jobsheet_table.heading("mobile", text="Mobile")
            jobsheet_table.heading("address", text="Address")
            jobsheet_table.heading("brand", text="brand")
            jobsheet_table.heading("Cap", text="capacity")
            jobsheet_table.heading("Mech", text="Mechanic")
            jobsheet_table.heading("helper", text="Helper")
            jobsheet_table.heading("tin", text="Time In")
            jobsheet_table.heading("tout", text="Time Out")
            jobsheet_table.heading("desc", text="Desc")
            jobsheet_table.heading("materials", text="Materials")
            jobsheet_table.heading("charge", text="Charge")
            jobsheet_table.heading("expense", text="Expense")
            jobsheet_table.heading("zone", text="Zone")
            jobsheet_table["show"] = "headings"

            jobsheet_table.column("jobid", width=40)
            jobsheet_table.column("date", width=70)
            jobsheet_table.column("name", width=100)
            jobsheet_table.column("mobile", width=100)
            jobsheet_table.column("address", width=100)
            jobsheet_table.column("brand", width=100)
            jobsheet_table.column("Cap", width=100)
            jobsheet_table.column("Mech", width=100)
            jobsheet_table.column("helper", width=100)
            jobsheet_table.column("tin", width=100)
            jobsheet_table.column("tout", width=100)
            jobsheet_table.column("desc", width=100)
            jobsheet_table.column("materials", width=100)
            jobsheet_table.column("charge", width=100)
            jobsheet_table.column("expense", width=100)
            jobsheet_table.column("zone", width=100)
            jobsheet_table.pack(fill=BOTH, expand=1)
            rowsDisplay = searchDateRange()
            count = 0
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
                count += 1
            ety.insert(0, count)
        def search_btn_command(searchBy,searchKey):
            for widgets in f2.winfo_children():
                widgets.destroy()
            if searchBy == 'Job ID':
                if searchKey == "":
                    all_jobsheet()
                else:
                    search_from_jobsheet(searchKey)
            elif searchBy == 'Customer ID':
                search_by_cust(searchKey)
            elif searchBy == 'Employee ID':
                search_by_emp(searchKey)
            elif searchBy == "Date":
                search_by_date(searchKey)
            elif searchBy == 'Date Range':
                search_by_date_range(searchKey)
            elif searchKey in zone_list:
                search_by_zone(searchKey)
            elif searchBy == 'Zone & Date':
                search_by_zoneDate(searchKey)
            elif searchBy == 'Zone & Date Range':
                search_by_zoneDateRange(searchKey)

        home_frame = tk.Frame(main_frame,bg='#1e81b0', highlightthickness=1)
        home_frame.configure(height=fheight, width=900)
        home_frame.pack(side='left')
        home_frame.pack_propagate(False)
        f1=tk.Frame(home_frame,bg='#1e81b0', highlightthickness=2,bd=4, highlightbackground='white',relief='raised')
        f1.configure(height=250, width=700,)
        f1.pack_propagate(False)
        f1.pack(side='top',fill='both')
        f2 = tk.Frame(home_frame, bg='grey', highlightthickness=4, highlightbackground='grey')
        f2.configure(height=630, width=900)
        f2.propagate(False)
        f2.pack(fill='both')
#-----------------       search button and search bar   ------------------------------------------
        search_list = ['Job ID', 'Customer ID', 'Employee ID', 'Date', 'Date Range', 'Zone', 'Zone & Date','Zone & Date Range']
        searchBy=ctk.CTkComboBox(f1,width=200,values=search_list,corner_radius=40,height=40,)
        searchBy.grid(row=0, column=0,columnspan=2,padx=10,pady=7)
        searchKey=ctk.CTkEntry(f1,width=490,corner_radius=40,height=40)
        searchKey.grid(row=0, column=3)
        search_btn=ctk.CTkButton(f1,text='Search',corner_radius=40,height=40,command=lambda :search_btn_command(searchBy.get(),searchKey.get()))
        search_btn.grid(row=0,column=4,padx=10,pady=5)

        todo_frame=tk.Frame(main_frame,bg='grey', highlightthickness=2, highlightbackground='white')
        todo_frame.configure(height=fheight, width=250)
        todo_frame.pack(side='right')

        def todo_list():
            task = StringVar()
            task_entry = Entry(todo_frame, width='20', font='arial 14', bd=1)
            task_entry.place(x=5, y=550)
            task_entry.focus()
            task_list = []

            def openTaskFile():
                with open("tasklist.txt", "r") as taskfile:
                    tasks = taskfile.readlines()
                for task in tasks:
                    if task != '\n':
                        task_list.append(task)
                        listbox.insert(END, task)
            def addTask():
                task = " "+task_entry.get()
                task_entry.delete(0, END)
                if task:
                    with open('tasklist.txt', 'a') as taskfile:
                        taskfile.write(f"\n{task}")
                    task_list.append(task)
                    listbox.insert(END, task)
            def deleteTask():
                task = str(listbox.get(ANCHOR))
                if task in task_list:
                    task_list.remove(task)
                    with open("tasklist.txt", 'w') as taskfile:
                        for task in task_list:
                            taskfile.write(task + "\n")
                    listbox.delete(ANCHOR)

            listbox = Listbox(todo_frame, font=('arial', 12), width=24, height=27)
            listbox.place(x=5, y=5)
            scroll_v = ctk.CTkScrollbar(todo_frame, height=542)
            scroll_v.place(x=227, y=5)
            listbox.configure(yscrollcommand=scroll_v.set)
            scroll_v.configure(command=listbox.yview)
            scroll_h = ctk.CTkScrollbar(todo_frame, orientation='horizontal', width=226)
            scroll_h.place(x=5, y=530)
            listbox.configure(xscrollcommand=scroll_h.set)
            scroll_h.configure(command=listbox.xview)
            add_task_button = ctk.CTkButton(todo_frame, width=220, text='Add', corner_radius=100, command=addTask)
            add_task_button.place(x=5, y=590)
            del_task_button = ctk.CTkButton(todo_frame, width=220, text='Delete', corner_radius=100, command=deleteTask)
            del_task_button.place(x=5, y=630)
            openTaskFile()
        todo_list()
# ======================================================================================================================
    def js_page():
        def connect():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS jobsheet (job_id text PRIMARY KEY, date INTEGER, cust_name text,mobile bigint, address text,
                brand TEXT, acType text, mech text, helper text,
                time_in integer, time_out integer, desc text, materials text, amount mediumint, expense mediumint, zone text  )''')
            conn.commit()
            conn.close()
        def jsinsert(jobid, date, name,mobile,address,brand,acType,mech,helper,tin,tout,desc,materials,charge,expense,zone):
            try:
                connect()
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute("INSERT INTO jobsheet VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (jobid, date, name,mobile,address,brand,acType,mech,helper,tin,tout,desc,materials,charge,expense,zone))

                conn.commit()
                conn.close()
            except Exception as e:
                print(e)
        def jsview():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM jobsheet")
            rows = cur.fetchall()
            rows.reverse()
            conn.close()
            return rows
        def jsdelete(jobid):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM jobsheet WHERE job_id =?", (jobid,))
            conn.commit()
            conn.close()
        def jsupdate(jobid, brand, acType, mechanic, helper, charge,expense,tin,tout,desc,zone,materials):
            try:
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                cur.execute(
                    "UPDATE jobsheet SET brand=?, acType=?,mech=?, helper=?, time_in=?, time_out=?, desc=?, "
                    "materials=?, amount=?, expense=?,zone=? WHERE job_id=?",
                    (brand, acType, mechanic, helper, tin, tout, desc, materials, charge, expense, zone, jobid))
                conn.commit()
                conn.close()
            except:
                print("error")
        def js_get_selection():
            print('get selected')
            sel=jobsheet_table.selection()
            for i in sel:
                c_i=jobsheet_table.item(i)
                c_v=c_i.get("values")
                print(c_v)
                print
                jobid.insert(0,c_v[0])
                name.insert(0,c_v[2])
                address.insert(0,c_v[4])
                tin.insert(0,c_v[9])
                desc.insert(0,c_v[11])
                materials.insert(0,c_v[12])
                charge.insert(0,c_v[13])
                date_.insert(0,c_v[1])
                mobile.insert(0,c_v[3])
                tout.insert(0,c_v[10])
                expense.insert(0,c_v[14])
                brand.set(c_v[5])
                acType.set(c_v[6])
                mech.set(c_v[7])
                helper.set(c_v[8])
                zone.set(c_v[15])

        jsframe = tk.Frame(main_frame, bg='grey', highlightthickness=4, highlightbackground='white')
        jsframe.pack(fill='both')
        #jsframe.configure(height=fheight, width=200, bd=2, relief="raised",)
        #============================   tree view table   =====================================
        table_frame= tk.Frame(main_frame,highlightbackground='pink',bg='green')
        table_frame.pack(fill='y')
        style=ttk.Style()
        style.theme_use('clam')
        style.configure('mystyle.Treeview',font=('Calibri',10))

        jobsheet_table=ttk.Treeview(table_frame,style="mystyle.Treeview",columns=("jobid","date","name","mobile","address","brand","Cap","Mech",
                                                         "helper","tin","tout","desc","materials","charge","expense","zone"))

        scv = ctk.CTkScrollbar(table_frame,)
        scv.pack(side='right',fill=Y)
        jobsheet_table.configure(yscrollcommand=scv.set)
        scv.configure(command=jobsheet_table.yview)
        sch = ctk.CTkScrollbar(table_frame, orientation='horizontal',)
        sch.pack(side='bottom',fill=X)
        jobsheet_table.configure(xscrollcommand=sch.set)
        sch.configure(command=jobsheet_table.xview)

        jobsheet_table.heading("jobid",text="Jid")
        jobsheet_table.heading("date", text="Date")
        jobsheet_table.heading("name", text="Name")
        jobsheet_table.heading("mobile", text="Mobile")
        jobsheet_table.heading("address", text="Address")
        jobsheet_table.heading("brand", text="brand")
        jobsheet_table.heading("Cap", text="capacity")
        jobsheet_table.heading("Mech", text="Mechanic")
        jobsheet_table.heading("helper", text="Helper")
        jobsheet_table.heading("tin", text="Time In")
        jobsheet_table.heading("tout", text="Time Out")
        jobsheet_table.heading("desc", text="Desc")
        jobsheet_table.heading("materials", text="Materials")
        jobsheet_table.heading("charge", text="Charge")
        jobsheet_table.heading("expense", text="Expense")
        jobsheet_table.heading("zone", text="Zone")
        jobsheet_table["show"]="headings"

        jobsheet_table.column("jobid", width=40)
        jobsheet_table.column("date", width=70)
        jobsheet_table.column("name", width=100)
        jobsheet_table.column("mobile", width=100)
        jobsheet_table.column("address", width=100)
        jobsheet_table.column("brand", width=100)
        jobsheet_table.column("Cap", width=100)
        jobsheet_table.column("Mech", width=100)
        jobsheet_table.column("helper", width=100)
        jobsheet_table.column("tin", width=100)
        jobsheet_table.column("tout", width=100)
        jobsheet_table.column("desc", width=100)
        jobsheet_table.column("materials", width=100)
        jobsheet_table.column("charge", width=100)
        jobsheet_table.column("expense", width=100)
        jobsheet_table.column("zone", width=100)

        jobsheet_table.pack(fill='y',expand=1)
        #======================                  labels                 ======================================================
        def labels():
            jobid_lb = ctk.CTkLabel(jsframe, text='Job ID', font=('arial', 16))
            jobid_lb.grid(row=0, column=0, padx=10)
            cname_lb = ctk.CTkLabel(jsframe, text="Name", font=("arial", 16))
            cname_lb.grid(row=1, column=0, padx=10)
            address_lb = ctk.CTkLabel(jsframe, text="Address", font=("arial", 16))
            address_lb.grid(row=2, column=0, padx=10)
            ac_lb = ctk.CTkLabel(jsframe, text="Brand", font=("arial", 16))
            ac_lb.grid(row=3, column=0, padx=10)
            mech_lb = ctk.CTkLabel(jsframe, text="Mechanic", font=('arial', 16))
            mech_lb.grid(row=4, column=0, padx=10)
            tin_lb = ctk.CTkLabel(jsframe, text="Time In", font=('arial', 16))
            tin_lb.grid(row=5, column=0, padx=10)
            desc_lb = ctk.CTkLabel(jsframe, text="Description", font=('arial', 16))
            desc_lb.grid(row=6, column=0, padx=10)
            mat_lb = ctk.CTkLabel(jsframe, text="Materials", font=('arial', 16))
            mat_lb.grid(row=7, column=0, padx=10)
            amt_lb = ctk.CTkLabel(jsframe, text="Charge", font=('arial', 16))
            amt_lb.grid(row=8, column=0, padx=10)
            zone_lb = ctk.CTkLabel(jsframe, text="Zone", font=('arial', 16))
            zone_lb.grid(row=9, column=0, padx=10)
            # ============================           column 2 labels              ================================
            date_lb = ctk.CTkLabel(jsframe, text="Date", font=("arial", 16))
            date_lb.grid(row=0, column=2, padx=10)
            number_lb = ctk.CTkLabel(jsframe, text="Mobile", font=("arial", 16))
            number_lb.grid(row=1, column=2, padx=10)
            ac_type_lb = ctk.CTkLabel(jsframe, text="Capacity", font=('arial', 16))
            ac_type_lb.grid(row=3, column=2, padx=10)
            hlpr_lb = ctk.CTkLabel(jsframe, text="Helper", font=('arial', 16))
            hlpr_lb.grid(row=4, column=2, padx=10)
            tout_lb = ctk.CTkLabel(jsframe, text="Time Out", font=('arial', 16))
            tout_lb.grid(row=5, column=2, padx=10)
            exp_lb = ctk.CTkLabel(jsframe, text='Expense', font=('arial', 16))
            exp_lb.grid(row=8, column=2, padx=10)
        labels()

        #================    Entries       ===============================================================================
        jobid = ctk.CTkEntry(jsframe, font=("arial", 14), width=240, placeholder_text="Enter Job ID")
        jobid.grid(row=0, column=1, padx=10, pady=4)
        name = ctk.CTkEntry(jsframe, font=("arial", 14), placeholder_text="enter customer name", width=240)
        name.grid(row=1, column=1, padx=10, pady=4)
        address = ctk.CTkEntry(jsframe, font=("arial", 14), width=675, placeholder_text="enter customer address")
        address.grid(row=2, column=1, columnspan=3, padx=10, pady=4)
        brand = ctk.CTkComboBox(jsframe, values=ac_brand_list, width=240)
        brand.grid(row=3, column=1, padx=10, pady=4)
        mech = ctk.CTkComboBox(jsframe, values=mechanic_list, width=240)
        mech.grid(row=4, column=1, padx=10, pady=4)
        tin = ctk.CTkEntry(jsframe, font=('arial', 14), width=240, placeholder_text="Enter Time in")
        tin.grid(row=5, column=1, padx=10, pady=4)
        desc = ctk.CTkEntry(jsframe, font=('arial', 14), width=675, placeholder_text="Describe details of fault")
        desc.grid(row=6, column=1, padx=10, pady=4, columnspan=3)
        materials = ctk.CTkEntry(jsframe, font=('arial', 14), width=675, placeholder_text="Materials")
        materials.grid(row=7, column=1, padx=10, pady=4, columnspan=3)
        charge = ctk.CTkEntry(jsframe, font=('arial', 14), width=240, placeholder_text="Enter Charged amount")
        charge.grid(row=8, column=1, padx=10, pady=4)
        zone = ctk.CTkComboBox(jsframe, values=zone_list, width=240)
        zone.grid(row=9, column=1, padx=10, pady=4)
        date_ = ctk.CTkEntry(jsframe, width=240, placeholder_text="DD/MM/YY")
        date_.grid(row=0, column=3, padx=10)
        mobile = ctk.CTkEntry(jsframe, width=240, placeholder_text="Mobile")
        mobile.grid(row=1, column=3, padx=10)
        acType = ctk.CTkComboBox(jsframe, width=240, values=ac_cap_list)
        acType.grid(row=3, column=3, padx=10)
        helper = ctk.CTkComboBox(jsframe, width=240, values=helper_list)
        helper.grid(row=4, column=3, padx=10)
        tout = ctk.CTkEntry(jsframe, width=240, placeholder_text="Time Out")
        tout.grid(row=5, column=3, padx=10)
        expense = ctk.CTkEntry(jsframe, width=240, placeholder_text="Expense")
        expense.grid(row=8, column=3, padx=10)

        # ==============================      Buttons & Functions    ===============================================
        def reset_command():
            def clear_all():
                for item in jobsheet_table.get_children():
                    jobsheet_table.delete(item)
            clear_all()
            for widget in jsframe.winfo_children():
                if isinstance(widget, ctk.CTkEntry):
                    widget.delete(0, 'end')
            show_records()
        def show_records():
            rowsDisplay = jsview()
            for record in rowsDisplay:
                jobsheet_table.insert("", 'end', text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5], record[6], record[7], record[8]
                                              , record[9], record[10], record[11], record[12]
                                              , record[13], record[14], record[15]))
        def enter_command():
            jsinsert(jobid.get(), date_.get(), name.get(), mobile.get(), address.get(), brand.get(), acType.get(),
                     mech.get(), helper.get(),
                     tin.get(), tout.get(), desc.get(), materials.get(), charge.get(), expense.get(), zone.get())
            reset_command()
        def delete_command():
            obj = jobid.get()
            jsdelete(obj)
            reset_command()
        def update_command():
            jsupdate(jobid.get(), brand.get(), acType.get(), mech.get(), helper.get(),
                     charge.get(), expense.get(), tin.get(), tout.get(),
                     desc.get(), zone.get(), materials.get())
            reset_command()
        def buttons_on_right():
            button1 = ctk.CTkButton(jsframe, text='Enter data', width=200, height=60, command=enter_command,corner_radius=80)
            button1.grid(row=6, column=4, rowspan=2)
            button2 = ctk.CTkButton(jsframe, text='Clear Entries', width=200, height=60, command=reset_command,corner_radius=80)
            button2.grid(row=2, column=4, rowspan=2)
            button3 = ctk.CTkButton(jsframe, text='Update', width=200, height=60, command=update_command,corner_radius=80)
            button3.grid(row=4, column=4, rowspan=2)
            button4 = ctk.CTkButton(jsframe, text='Delete', width=200, height=60, command=delete_command ,corner_radius=80)
            button4.grid(row=0, column=4, rowspan=2)
            button5 = ctk.CTkButton(jsframe, text="Select", command=js_get_selection, width=200, height=60,corner_radius=80)
            button5.grid(row=8, column=4, rowspan=2)
        show_records()
        buttons_on_right()

        for widget in jsframe.winfo_children():
            widget.grid_configure(padx=14, pady=8,sticky='w')
# ===========================================================================================================================

    def csd_page():

        csdFrame = tk.Frame(main_frame)
        csdFrame.pack()
        tabview = ctk.CTkTabview(csdFrame, height=fheight, width=1200)
        tabview.add("Add Customer")
        tabview.add("Add Employee")
        tabview.add("Add Rental")
        t1 = tabview.tab("Add Customer")
        t2 = tabview.tab("Add Employee")
        t3 = tabview.tab("Add Rental")

        def csdConnect():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                '''CREATE TABLE IF NOT EXISTS customer_details (cust_name text,mobile bigint PRIMARY KEY, address text,
                                                                brand text, acType text, info text)''')
            conn.commit()
            conn.close()

        def csdInsert(name, mobile, address, brand, acType, info):
            #   try:
            csdConnect()
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO customer_details VALUES (?,?,?,?,?,?)",
                        (name, mobile, address, brand, acType, info))

            conn.commit()
            conn.close()
            #  except:
            #      print("error")

        def csdView():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM customer_details")
            rows = cur.fetchall()
            rows.reverse()
            conn.close()
            return rows

        def csdDelete(number):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM customer_details WHERE mobile=?", (number,))
            conn.commit()
            conn.close()

        def csdUpdate(cbrand, cAcType, caddress, info, number):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                "UPDATE customer_details SET brand=?, acType=?,address=?, info=? WHERE mobile=?",
                (cbrand, cAcType, caddress, info, number))
            conn.commit()
            conn.close()

        # .............................. Add Customer .....................................................................
        upperFrame = ctk.CTkFrame(t1, height=600, width=800)
        upperFrame.pack(side='top', anchor='w')
        cName_lb = ctk.CTkLabel(upperFrame, text="Name")
        cName_lb.grid(row=0, column=0, ipadx=40)
        cMobile_lb = ctk.CTkLabel(upperFrame, text="Mobile")
        cMobile_lb.grid(row=1, column=0)
        cAddress_lb = ctk.CTkLabel(upperFrame, text="Address")
        cAddress_lb.grid(row=2, column=0)
        cBrand_lb = ctk.CTkLabel(upperFrame, text="Brand")
        cBrand_lb.grid(row=3, column=0)
        cAcType_lb = ctk.CTkLabel(upperFrame, text="Capacity")
        cAcType_lb.grid(row=4, column=0)
        cAcType_lb = ctk.CTkLabel(upperFrame, text="Information")
        cAcType_lb.grid(row=5, column=0)

        cName = ctk.CTkEntry(upperFrame, width=240, placeholder_text="Name")
        cName.grid(row=0, column=1, columnspan=2)
        cMobile = ctk.CTkEntry(upperFrame, width=240, placeholder_text="Mobile")
        cMobile.grid(row=1, column=1, columnspan=2)
        cAddress = ctk.CTkEntry(upperFrame, width=240, placeholder_text="Address")
        cAddress.grid(row=2, column=1, columnspan=2)
        cBrand = ctk.CTkComboBox(upperFrame, width=240, values=ac_brand_list)
        cBrand.grid(row=3, column=1, columnspan=2)
        cAcType = ctk.CTkComboBox(upperFrame, width=240, values=ac_cap_list)
        cAcType.grid(row=4, column=1, columnspan=2)
        cAddInfo = ctk.CTkEntry(upperFrame, width=240, placeholder_text="Additional Information")
        cAddInfo.grid(row=5, column=1, columnspan=2)
        # =====================================================================
        customer_table = ttk.Treeview(t1, columns=("name", "mobile", "address", "brand", "Cap", "Info"))
        ct_sc_v = ctk.CTkScrollbar(t1, height=150)
        ct_sc_v.pack(side='right', fill=Y)
        # ct_sc_v.grid(row=0, column=2, rowspan=2)
        customer_table.configure(yscrollcommand=ct_sc_v.set)
        ct_sc_v.configure(command=customer_table.yview)
        ct_sc_h = ctk.CTkScrollbar(t1, orientation='horizontal', width=240)
        ct_sc_h.pack(side='bottom', fill=X)
        # ct_sc_h.grid(row=5, column=0, columnspan=2)
        customer_table.configure(xscrollcommand=ct_sc_h.set)
        ct_sc_h.configure(command=customer_table.xview)
        # ========
        customer_table.heading("name", text="Name")
        customer_table.heading("mobile", text="Mobile")
        customer_table.heading("address", text="Address")
        customer_table.heading("brand", text="brand")
        customer_table.heading("Cap", text="capacity")
        customer_table.heading("Info", text="addInfo")
        customer_table["show"] = "headings"
        customer_table.column("name", width=100)
        customer_table.column("mobile", width=100)
        customer_table.column("address", width=100)
        customer_table.column("brand", width=100)
        customer_table.column("Cap", width=100)
        customer_table.column("Info", width=100)
        customer_table.pack(fill=BOTH, expand=1)

        def csd_show_records():
            rowsDisplay = csdView()
            for record in rowsDisplay:
                customer_table.insert("", 'end', text=record[0],
                                      values=(record[0], record[1], record[2], record[3], record[4]
                                              , record[5]))

        def csd_reset_command():
            def csd_clear_all():
                for item in customer_table.get_children():
                    customer_table.delete(item)

            csd_clear_all()
            for widget in upperFrame.winfo_children():
                if isinstance(widget, ctk.CTkEntry):
                    widget.delete(0, 'end')
            csd_show_records()

        def csd_enter_command():
            csdInsert(cName.get(), cMobile.get(), cAddress.get(), cBrand.get(), cAcType.get(), cAddInfo.get())
            csd_reset_command()

        def csd_delete_command():
            obj = cMobile.get()
            csdDelete(obj)
            csd_reset_command()

        def csd_update_command():
            csdUpdate(cBrand.get(), cAcType.get(), cAddress.get(), cAddInfo.get(), cMobile.get())
            csd_reset_command()

        # csd_reset_command()
        c_b1 = ctk.CTkButton(upperFrame, text="Enter Data", command=csd_enter_command)
        c_b1.grid(row=6, column=0)
        c_b2 = ctk.CTkButton(upperFrame, text="Update", command=csd_update_command)
        c_b2.grid(row=6, column=1)
        c_b3 = ctk.CTkButton(upperFrame, text="Delete ", command=csd_delete_command)
        c_b3.grid(row=6, column=2)
        # *******************************************************************************************

        for widgets in upperFrame.winfo_children():
            widgets.grid_configure(padx=20, pady=10)
        csd_show_records()

        # .....................................................................................................................

        # ====================   ADD EMPLOYEE          =======================================
        def empConnect():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS employee_details (emp_id text PRIMARY KEY, emp_name text, mobile bigint, address text,
                                                                        con_person text,contact bigint, designation text, salary int,
                                                                        blood_group text, info text, id_proof text)''')
            conn.commit()
            conn.close()

        def empInsert(eID, eName, eMobile, eAddress, eNominee, eNominCont, eDesig, eSalary, bGroup, eInfo, eIdProof):
            # try:
            empConnect()
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO employee_details VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (eID, eName, eMobile, eAddress, eNominee, eNominCont, eDesig, eSalary, bGroup, eInfo, eIdProof))

            conn.commit()
            conn.close()

        # except:
        #   print("error")
        def empView():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM employee_details")
            rows = cur.fetchall()
            rows.reverse()
            conn.close()
            return rows

        def empDelete(empID):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM employee_details WHERE emp_id=?", (empID,))
            conn.commit()
            conn.close()

        def empUpdate(eMobile, eAddress, eNominee, eNominCont, eDesig, eSalary, bGroup, eInfo, eID):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                "UPDATE employee_details SET mobile=?, address=?,con_person=?,contact=?, designation=?,salary=?,"
                "blood_group=?,id_proof=? WHERE emp_id=?",
                (eMobile, eAddress, eNominee, eNominCont, eDesig, eSalary, bGroup, eInfo, eID))
            conn.commit()
            conn.close()

        # empConnect()
        eUpperFrame = ctk.CTkFrame(t2, height=600, width=800)
        eUpperFrame.pack(side='top', anchor='w')
        eId_lb = ctk.CTkLabel(eUpperFrame, text="Employee ID")
        eId_lb.grid(row=0, column=0)
        eName_lb = ctk.CTkLabel(eUpperFrame, text="Name")
        eName_lb.grid(row=1, column=0, ipadx=40)
        eMobile_lb = ctk.CTkLabel(eUpperFrame, text="Mobile")
        eMobile_lb.grid(row=2, column=0)
        eAddress_lb = ctk.CTkLabel(eUpperFrame, text="Address")
        eAddress_lb.grid(row=3, column=0)
        eNominee_lb = ctk.CTkLabel(eUpperFrame, text="Nominee Name")
        eNominee_lb.grid(row=4, column=0)
        eNomin_lb = ctk.CTkLabel(eUpperFrame, text="Nominee Contact")
        eNomin_lb.grid(row=5, column=0)
        eDesig_lb = ctk.CTkLabel(eUpperFrame, text="Designation")
        eDesig_lb.grid(row=6, column=0)
        bgroup_lb = ctk.CTkLabel(eUpperFrame, text="Blood group")
        bgroup_lb.grid(row=0, column=4)
        einfo_lb = ctk.CTkLabel(eUpperFrame, text="Information")
        einfo_lb.grid(row=1, column=4)
        eSalary_lb = ctk.CTkLabel(eUpperFrame, text="Salary")
        eSalary_lb.grid(row=4, column=4)
        eId_Pr_lb = ctk.CTkLabel(eUpperFrame, text="Id Proof")
        eId_Pr_lb.grid(row=5, column=4)
        # ..........................................................................................................................................
        eID = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="employee id")
        eID.grid(row=0, column=1, columnspan=2)
        eName = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Name")
        eName.grid(row=1, column=1, columnspan=2)
        eMobile = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Mobile")
        eMobile.grid(row=2, column=1, columnspan=2)
        eAddress = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Address")
        eAddress.grid(row=3, column=1, columnspan=2)
        eNominee = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Nominee Name")
        eNominee.grid(row=4, column=1, columnspan=2)
        eNominCont = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Nominee Contact Number")
        eNominCont.grid(row=5, column=1, columnspan=2)
        eDesig = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Designation")
        eDesig.grid(row=6, column=1, columnspan=2)
        eSalary = ctk.CTkEntry(eUpperFrame, width=240, placeholder_text="Salary")
        eSalary.grid(row=4, column=5, columnspan=2)
        bGroup = ctk.CTkEntry(eUpperFrame, width=240, )
        bGroup.grid(row=0, column=5, columnspan=2)
        eInfo = ctk.CTkEntry(eUpperFrame, width=240, height=120)
        eInfo.grid(row=1, column=5, rowspan=3, columnspan=2)
        eIdProof = ctk.CTkEntry(eUpperFrame, width=150, placeholder_text='Aadhar Number')
        eIdProof.grid(row=5, column=5)
        e = ctk.CTkButton(eUpperFrame, text="button", width=50)
        e.grid(row=5, column=6)
        # ==========================================================================================\
        emp_table = ttk.Treeview(t2, columns=(
        "eID", "eName", "eMobile", "eAddress", "eNominee", "eNominCont", "eDesig", "eSalary", "bGroup", "eInfo"))
        et_sc_v = ctk.CTkScrollbar(t2, height=150)
        et_sc_v.pack(side='right', fill=Y)
        emp_table.configure(yscrollcommand=et_sc_v.set)
        et_sc_v.configure(command=emp_table.yview)
        et_sc_h = ctk.CTkScrollbar(t2, orientation='horizontal', width=240)
        et_sc_h.pack(side='bottom', fill=X)
        emp_table.configure(xscrollcommand=et_sc_h.set)
        et_sc_h.configure(command=emp_table.xview)

        emp_table.heading("eID", text="ID")
        emp_table.heading("eName", text="Name")
        emp_table.heading("eMobile", text="Mobile")
        emp_table.heading("eAddress", text="Address")
        emp_table.heading("eNominee", text="Nominee")
        emp_table.heading("eNominCont", text="Nominee No")
        emp_table.heading("eDesig", text="Designation")
        emp_table.heading("eSalary", text="Salary")
        emp_table.heading("bGroup", text="B Group")
        emp_table.heading("eInfo", text="Info")
        emp_table["show"] = "headings"
        emp_table.column("eID", width=100)  # 1
        emp_table.column("eName", width=100)  # 2
        emp_table.column("eMobile", width=100)  # 3
        emp_table.column("eAddress", width=100)  # 4
        emp_table.column("eNominee", width=100)  # 5
        emp_table.column("eNominCont", width=100)  # 6
        emp_table.column("eDesig", width=100)  # 7
        emp_table.column("eSalary", width=100)  # 8
        emp_table.column("bGroup", width=50)  # 9
        emp_table.column("eInfo", width=100)  # 10
        emp_table.pack(fill=BOTH, expand=1)

        def emp_show_records():
            rowsDisplay = empView()
            for record in rowsDisplay:
                emp_table.insert("", 'end', text=record[0],
                                 values=(record[0], record[1], record[2], record[3], record[4]
                                         , record[5], record[6], record[7], record[8], record[9]))
        def emp_reset_command():
            def emp_clear_all():
                for item in emp_table.get_children():
                    emp_table.delete(item)

            emp_clear_all()
            for widget in eUpperFrame.winfo_children():
                if isinstance(widget, ctk.CTkEntry):
                    widget.delete(0, 'end')
            emp_show_records()
        def emp_enter_command():
            empInsert(eID.get(), eName.get(), eMobile.get(), eAddress.get(), eNominee.get(), eNominCont.get(),
                      eDesig.get(), eSalary.get(), bGroup.get(), eInfo.get(), eIdProof.get())
            emp_reset_command()
        def emp_delete_command():
            obj = eID.get()
            empDelete(obj)
            emp_reset_command()
        def emp_update_command():
            empUpdate(eMobile.get(), eAddress.get(), eNominee.get(), eNominCont.get(), eDesig.get(), eSalary.get(),
                      bGroup.get(), eInfo.get(), eID.get())
            emp_reset_command()
        emp_reset_command()
        e_b1 = ctk.CTkButton(eUpperFrame, text="Add Employee", command=emp_enter_command)
        e_b1.grid(row=7, column=0)
        e_b2 = ctk.CTkButton(eUpperFrame, text="Update Employee", command=emp_update_command)
        e_b2.grid(row=7, column=1)
        e_b3 = ctk.CTkButton(eUpperFrame, text="Delete Employee", command=emp_delete_command)
        e_b3.grid(row=7, column=2)

        for widgets in eUpperFrame.winfo_children():
            widgets.grid_configure(padx=20, pady=10)

        # ======================= ADD RENTAL      =============================
        rupperFrame = ctk.CTkFrame(t3, height=600, width=800)
        rupperFrame.pack(side='top', anchor='w')
        r_lb = ctk.CTkLabel(rupperFrame, text="Rental ID")
        r_lb.grid(row=0, column=0, ipadx=20)
        rName_lb = ctk.CTkLabel(rupperFrame, text="Name")
        rName_lb.grid(row=1, column=0, ipadx=20)
        rMobile_lb = ctk.CTkLabel(rupperFrame, text="Mobile")
        rMobile_lb.grid(row=2, column=0)
        rAddress_lb = ctk.CTkLabel(rupperFrame, text="Address")
        rAddress_lb.grid(row=3, column=0)
        rInfo_lb = ctk.CTkLabel(rupperFrame, text="Info")
        rInfo_lb.grid(row=4, column=0)
        rInsOn_lb = ctk.CTkLabel(rupperFrame, text="Installed On")
        rInsOn_lb.grid(row=5, column=0)
        rDeposit_lb = ctk.CTkLabel(rupperFrame, text="Deposit")
        rDeposit_lb.grid(row=0, column=3)
        rInsCha_lb = ctk.CTkLabel(rupperFrame, text="Installation Charge")
        rInsCha_lb.grid(row=1, column=3)
        rRent_lb = ctk.CTkLabel(rupperFrame, text="Rent")
        rRent_lb.grid(row=2, column=3)
        rIU_lb = ctk.CTkLabel(rupperFrame, text="Indoor Unit")
        rIU_lb.grid(row=3, column=3)
        rOU_lb = ctk.CTkLabel(rupperFrame, text="Outdoor Unit")
        rOU_lb.grid(row=4, column=3)

        rId = ctk.CTkEntry(rupperFrame, placeholder_text="Rental ID", width=200)
        rId.grid(row=0, column=1, ipadx=20)
        rName = ctk.CTkEntry(rupperFrame, placeholder_text="Name", width=200)
        rName.grid(row=1, column=1, ipadx=20)
        rMobile = ctk.CTkEntry(rupperFrame, placeholder_text="Mobile", width=200)
        rMobile.grid(row=2, column=1, ipadx=20)
        rAddress = ctk.CTkEntry(rupperFrame, placeholder_text="Address", width=200)
        rAddress.grid(row=3, column=1, ipadx=20)
        rInfo = ctk.CTkEntry(rupperFrame, placeholder_text="Info", width=200)
        rInfo.grid(row=4, column=1, ipadx=20)
        rInsOn = ctk.CTkEntry(rupperFrame, placeholder_text="Installed On", width=200)
        rInsOn.grid(row=5, column=1, ipadx=20)
        rDeposit = ctk.CTkEntry(rupperFrame, placeholder_text="Deposit", width=200)
        rDeposit.grid(row=0, column=4, ipadx=20)
        rInsCharge = ctk.CTkEntry(rupperFrame, placeholder_text="Installation Charge", width=200)
        rInsCharge.grid(row=1, column=4, ipadx=20)
        rRent = ctk.CTkEntry(rupperFrame, placeholder_text="Rent", width=200)
        rRent.grid(row=2, column=4, ipadx=20)
        rIU = ctk.CTkEntry(rupperFrame, placeholder_text="Indoor Unit", width=200)
        rIU.grid(row=3, column=4, ipadx=20)
        rOU = ctk.CTkEntry(rupperFrame, placeholder_text="Outdoor Unit", width=200)
        rOU.grid(row=4, column=4, ipadx=20)

        # =====================================================================
        rental_ac_table = ttk.Treeview(t3, columns=(
        "rId", "rName", "rMobile", "rAddress", "rRent", "rInfo", "rInsOn", "rDeposit", "rInsCha", "rIU", "rOU"))
        rt_sc_v = ctk.CTkScrollbar(t3, height=150)
        rt_sc_v.pack(side='right', fill=Y)
        # ct_sc_v.grid(row=0, column=2, rowspan=2)
        rental_ac_table.configure(yscrollcommand=rt_sc_v.set)
        rt_sc_v.configure(command=rental_ac_table.yview)
        rt_sc_h = ctk.CTkScrollbar(t3, orientation='horizontal')
        rt_sc_h.pack(side='bottom', fill=X)
        # ct_sc_h.grid(row=5, column=0, columnspan=2)
        rental_ac_table.configure(xscrollcommand=rt_sc_h.set)
        rt_sc_h.configure(command=rental_ac_table.xview)
        # ========
        rental_ac_table.heading("rId", text="Rental ID")
        rental_ac_table.heading("rName", text="Name")
        rental_ac_table.heading("rMobile", text="Mobile")
        rental_ac_table.heading("rAddress", text="brand")
        rental_ac_table.heading("rRent", text="Rent")
        rental_ac_table.heading("rInfo", text="Info")
        rental_ac_table.heading("rInsOn", text="Installed On")
        rental_ac_table.heading("rDeposit", text="Deposit")
        rental_ac_table.heading("rInsCha", text="Installation Charge")
        rental_ac_table.heading("rIU", text="Outdoor Unit")
        rental_ac_table.heading("rOU", text="Indoor Unit")
        rental_ac_table["show"] = "headings"

        rental_ac_table.column("rId", width=100)
        rental_ac_table.column("rName", width=100)
        rental_ac_table.column("rMobile", width=100)
        rental_ac_table.column("rAddress", width=100)
        rental_ac_table.column("rRent", width=100)
        rental_ac_table.column("rInfo", width=100)
        rental_ac_table.column("rInsOn", width=100)
        rental_ac_table.column("rDeposit", width=100)
        rental_ac_table.column("rInsCha", width=100)
        rental_ac_table.column("rIU", width=100)
        rental_ac_table.column("rOU", width=100)

        rental_ac_table.pack(fill=BOTH, expand=1)

        def rConnect():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS rental_details (Rental_id text PRIMARY KEY, Name text, Mobile bigint, address text,
                                                                        Installed_on text,Deposit int, Installation_charge int, Rent int,
                                                                        Indoor_unit text, Outdoor_unit text, Info text)''')
            conn.commit()
            conn.close()
        def rInsert(rId, rName, rMobile, rAddress, rInsOn, rDepost, rInsCharge, rRent, rIU, rOU, rInfo):
            # try:
            rConnect()
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO rental_details VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (rId, rName, rMobile, rAddress, rInsOn, rDepost, rInsCharge, rRent, rIU, rOU, rInfo))

            conn.commit()
            conn.close()
        def rView():
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM rental_details")
            rows = cur.fetchall()
            rows.reverse()
            conn.close()
            return rows
        def rDelete(rID):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM rental_details WHERE Rental_id=?", (rID,))
            conn.commit()
            conn.close()
        def rUpdate(rName, rMobile, rAddress, rInsOn, rDeposit, rInsCharge, rRent, rIU, rOU, rInfo, rId):
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                "UPDATE rental_details SET Name=?,Mobile=?,Address=?,Installed_on=?,Deposit=?,Installation_charge=?, Rent=?,Indoor_unit=?,"
                "Outdoor_unit=?,Info=? WHERE Rental_id=?",
                (rName, rMobile, rAddress, rInsOn, rDeposit, rInsCharge, rRent, rIU, rOU, rInfo, rId))
            conn.commit()
            conn.close()
        def r_show_records():
            rowsDisplay = rView()
            for record in rowsDisplay:
                rental_ac_table.insert("", 'end', text=record[0],
                                       values=(record[0], record[1], record[2], record[3], record[4]
                                               , record[5]))
        def r_reset_command():
            def r_clear_all():
                for item in rental_ac_table.get_children():
                    rental_ac_table.delete(item)

            r_clear_all()
            for widget in rupperFrame.winfo_children():
                if isinstance(widget, ctk.CTkEntry):
                    widget.delete(0, 'end')
            r_show_records()
        def r_enter_command():
            rInsert(rId.get(), rName.get(), rMobile.get(), rAddress.get(), rInsOn.get(), rDeposit.get(),
                    rInsCharge.get(),
                    rRent.get(), rIU.get(), rOU.get(), rInfo.get())
            r_reset_command()
        def r_delete_command():
            obj = rId.get()
            rDelete(obj)
            r_reset_command()
        def r_update_command():
            rUpdate(rName.get(), rMobile.get(), rAddress.get(), rInsOn.get(), rDeposit.get(), rInsCharge.get(),
                    rRent.get(), rIU.get(), rOU.get(), rInfo.get(), rId.get())
            r_reset_command()

        r_b1 = ctk.CTkButton(rupperFrame, text="Enter Data", command=r_enter_command)
        r_b1.grid(row=8, column=0)
        r_b2 = ctk.CTkButton(rupperFrame, text="Update", command=r_update_command)
        r_b2.grid(row=8, column=1)
        r_b3 = ctk.CTkButton(rupperFrame, text="Delete ", command=r_delete_command)
        r_b3.grid(row=8, column=3)
        # *******************************************************************************************

        for widgets in rupperFrame.winfo_children():
            widgets.grid_configure(padx=20, pady=10)
        r_show_records()
        tabview.pack()
        # ========================================================================================================================

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()
        # =================== content FRAME(RIGHT)  ================

    con_width = (fwidth - 200)
    main_frame = tk.Frame(root, highlightthickness=2, )
    main_frame.pack()
    main_frame.pack_propagate(False)
    splash_image = ImageTk.PhotoImage(Image.open("ci_spalsh.png"))
    l1 = ctk.CTkLabel(master=main_frame, image=splash_image)
    l1.pack()
    main_frame.configure(height=fheight, width=con_width, bd=5, relief="raised")
    root.protocol("WM_DELETE_WINDOW", exit_)
    root.mainloop()


masterPage()
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("system")
root = ctk.CTk()
root.geometry("450x250")
root.title('Login')
root.iconbitmap("ci_logo.ico")

splash_image = ImageTk.PhotoImage(Image.open("ci_spalsh.png"))
frame = ctk.CTkFrame(master=root, width=320, height=200, border_width=1, corner_radius=20)
frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

entry1 = ctk.CTkEntry(master=frame, width=220, placeholder_text="username", corner_radius=20)
entry1.place(x=50, y=55)
entry2 = ctk.CTkEntry(master=frame, width=220, placeholder_text="password", show="*", corner_radius=20)
entry2.place(x=50, y=100)

login_button = ctk.CTkButton(master=frame, width=220, text="Login", corner_radius=40, command=login_button_function)
login_button.place(x=50, y=150)
root.mainloop()
