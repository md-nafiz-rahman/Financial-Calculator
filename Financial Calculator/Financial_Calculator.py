#Author : MD Nafiz Rahman (mnr10)
#Last Modified: 4th March 2022

from tkinter import *
import math
import numpy_financial as npf
mainWin = Tk()

mainWin.title("Finance Calculator")

descriptionLabel = Label(mainWin, text="This is a business financial calculator which consists of three menus.\nPlease select from the menu options below to choose your calculation", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

#This is the code for first menu

def openmenu1():
    menu1 = Toplevel()
    menu1.config(bg="#C9F7F9")
    menu1.title("Menu No. 1")
    menu1.iconbitmap("UOL.ico")
    menu1.geometry("550x350")

    def opensub_pr():
        sub_pr = Toplevel()
        sub_pr.config(bg="#C9F7F9")
        sub_pr.title("Profitability Ratios")
        sub_pr.iconbitmap("UOL.ico")
        sub_pr.geometry("550x600")

        prlbl1 = Label(sub_pr, text= "Please select what you want to calculate", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

        prvar1 = IntVar()
        prvar2 = IntVar()
        prvar3 = IntVar()

        check_gross_margin = Checkbutton(sub_pr, text="Gross Margin", variable=prvar1, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        check_operating_margin = Checkbutton(sub_pr, text="Operating Margin", variable=prvar2, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        check_netprofit_margin = Checkbutton(sub_pr, text="Net Profit Margin", variable=prvar3, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        empty_space1 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        sales_var = StringVar()
        gross_profit_var = StringVar()
        operating_income_var = StringVar()
        net_income_var = StringVar()

        sales_lbl = Label(sub_pr, text="Enter Total Sales",bg="#C9F7F9",font=("Arial", 10)).pack()

        sales_ent = Entry(sub_pr, textvariable = sales_var, bd=3).pack()

        gross_profit_lbl = Label(sub_pr, text="Enter Gross Profit",bg="#C9F7F9",font=("Arial", 10)).pack()

        gross_profit_ent = Entry(sub_pr, textvariable = gross_profit_var, bd=3).pack()

        operating_income_lbl = Label(sub_pr, text="Enter Operating Income",bg="#C9F7F9",font=("Arial", 10)).pack()

        operating_income_ent = Entry(sub_pr, textvariable = operating_income_var, bd=3).pack()

        net_income_lbl = Label(sub_pr, text="Enter Net Income",bg="#C9F7F9",font=("Arial", 10)).pack()

        net_income_ent = Entry(sub_pr, textvariable = net_income_var, bd=3).pack()

        empty_space2 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        def calc_pr():

            check_g_margin = int(prvar1.get())
            check_o_margin = int(prvar2.get())
            check_n_margin = int(prvar3.get())

            if (check_g_margin == 0) and (check_o_margin == 0) and (check_n_margin == 0):

                error_label_pr = Label(sub_pr, text="Please select a calculation", bg="#C9F7F9",font=("Arial", 10)).pack()

                return

            calc_sales = float(sales_var.get())
            calc_gross_profit = float(gross_profit_var.get())
            calc_operating_income = float(operating_income_var.get())
            calc_net_income = float(net_income_var.get())

            pr_gross_margin = calc_gross_profit / calc_sales

            pr_operating_margin = calc_operating_income / calc_sales

            pr_netprofit_margin = calc_net_income / calc_sales

            pr_gross_margin = round(pr_gross_margin, 2)

            pr_operating_margin = round(pr_operating_margin, 2)

            pr_netprofit_margin = round(pr_netprofit_margin, 2)

            if (check_g_margin == 1) and (check_o_margin == 0) and (check_n_margin == 0):
                empty1 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_gross_margin = Label(sub_pr, text="Your Gross Margin is "+ str(pr_gross_margin), bg="#C9F7F9", font=("Arial", 10) ).pack()

            if (check_g_margin == 0) and (check_o_margin == 1) and (check_n_margin == 0):
                empty_space7 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_operating_margin = Label(sub_pr, text="Your Operating Margin is "+ str(pr_operating_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_g_margin == 0) and (check_o_margin == 0) and (check_n_margin == 1):
                empty_space11 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_netprofit_margin = Label(sub_pr, text="Your Net Profit Margin is "+ str(pr_netprofit_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_g_margin == 1) and (check_o_margin == 1) and (check_n_margin == 0):
                empty_space4 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_gross_margin = Label(sub_pr, text="Your Gross Margin is "+ str(pr_gross_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()

                empty_space8 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

                result_operating_margin = Label(sub_pr, text="Your Operating Margin is "+ str(pr_operating_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_g_margin == 1) and (check_o_margin == 0) and (check_n_margin == 1):
                empty_space5 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_gross_margin = Label(sub_pr, text="Your Gross Margin is "+ str(pr_gross_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()
                empty_space12 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_netprofit_margin = Label(sub_pr, text="Your Net Profit Margin is "+ str(pr_netprofit_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_g_margin == 0) and (check_o_margin == 1) and (check_n_margin == 1):
                empty_space9 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_operating_margin = Label(sub_pr, text="Your Operating Margin is "+ str(pr_operating_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()
                empty_space13 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_netprofit_margin = Label(sub_pr, text="Your Net Profit Margin is "+ str(pr_netprofit_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_g_margin == 1) and (check_o_margin == 1) and (check_n_margin == 1):
                empty_space6 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_gross_margin = Label(sub_pr, text="Your Gross Margin is "+ str(pr_gross_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()
                empty_space10 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_operating_margin = Label(sub_pr, text="Your Operating Margin is "+ str(pr_operating_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()
                empty_space14 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                result_netprofit_margin = Label(sub_pr, text="Your Net Profit Margin is "+ str(pr_netprofit_margin),bg="#C9F7F9",font=("Arial", 10) ).pack()


        empty_space15 = Label(sub_pr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        calculate_pr_btn = Button(sub_pr, text="Calculate", command=calc_pr, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack()

        subpr_close_button = Button(sub_pr, text="Close Menu", command=sub_pr.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack(anchor="e")

    def opensub_lr():
        sub_lr = Toplevel()
        sub_lr.config(bg="#C9F7F9")
        sub_lr.title("Liquidity Ratios")
        sub_lr.iconbitmap("UOL.ico")
        sub_lr.geometry("550x600")

        #This is the code to calculate current ratio for the first menu second type
        lrlbl1 = Label(sub_lr, text= "Please select what you want to calculate", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

        lrvar1 = IntVar()
        lrvar2 = IntVar()
        lrvar3 = IntVar()

        check_current_ratio = Checkbutton(sub_lr, text="Current Ratio", variable=lrvar1, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        check_quick_ratio = Checkbutton(sub_lr, text="Quick Ratio", variable=lrvar2, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        check_cash_ratio = Checkbutton(sub_lr, text="Cash Ratio", variable=lrvar3, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        lr_current_assets = StringVar()
        lr_current_liabilities = StringVar()
        lr_inventory = StringVar()
        lr_cash = StringVar()

        empty_space1 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        lr_current_assets_lbl = Label(sub_lr, text="Enter Current Assets",bg="#C9F7F9",font=("Arial", 10)).pack()

        lr_current_assets_ent = Entry(sub_lr, textvariable = lr_current_assets,  bd=3).pack()

        lr_current_liabilities_lbl = Label(sub_lr, text="Enter Current Liabilities",bg="#C9F7F9",font=("Arial", 10)).pack()

        lr_current_liabilities_ent = Entry(sub_lr, textvariable = lr_current_liabilities,  bd=3).pack()

        lr_inventory_lbl = Label(sub_lr, text="Enter Inventory",bg="#C9F7F9",font=("Arial", 10)).pack()

        lr_inventory_ent = Entry(sub_lr, textvariable = lr_inventory,  bd=3).pack()

        lr_cash_lbl = Label(sub_lr, text="Enter Total Cash",bg="#C9F7F9",font=("Arial", 10)).pack()

        lr_cash_ent = Entry(sub_lr, textvariable = lr_cash,  bd=3).pack()

        def calc_lr():

            check_cr_ratio = int(lrvar1.get())
            check_q_ratio = int(lrvar2.get())
            check_ch_ratio = int(lrvar3.get())

            if (check_cr_ratio == 0) and (check_q_ratio == 0) and (check_ch_ratio == 0):

                error_label = Label(sub_lr, text="Please select a calculation", bg="#C9F7F9",font=("Arial", 10)).pack()

                return

            lr_cassets = float(lr_current_assets.get())
            lr_cliabilities = float(lr_current_liabilities.get())
            lr_cinventory = float(lr_inventory.get())
            lr_ccash = float(lr_cash.get())

            lr_current_ratio = lr_cassets / lr_cliabilities

            lr_quick_ratio = (lr_cassets - lr_cinventory) / lr_cliabilities

            lr_cash_ratio = lr_ccash / lr_cliabilities

            lr_current_ratio = round(lr_current_ratio, 2)

            lr_quick_ratio = round(lr_quick_ratio, 2)

            lr_cash_ratio = round(lr_cash_ratio, 2)

            if (check_cr_ratio == 1) and (check_q_ratio == 0) and (check_ch_ratio == 0):

                empty_space3 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_cr_ratio = Label(sub_lr, text="Your Current Ratio is "+ str(lr_current_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_cr_ratio == 0) and (check_q_ratio == 1) and (check_ch_ratio == 0):

                empty_space4 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_q_ratio = Label(sub_lr, text="Your Quick Ratio is "+ str(lr_quick_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_cr_ratio == 0) and (check_q_ratio == 0) and (check_ch_ratio == 1):

                empty_space13 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_ch_ratio = Label(sub_lr, text="Your Cash Ratio is "+ str(lr_cash_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_cr_ratio == 1) and (check_q_ratio == 1) and (check_ch_ratio == 0):

                empty_space5 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_cr_ratio = Label(sub_lr, text="Your Current Ratio is "+ str(lr_current_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

                empty_space10 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_q_ratio = Label(sub_lr, text="Your Quick Ratio is "+ str(lr_quick_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_cr_ratio == 1) and (check_q_ratio == 0) and (check_ch_ratio == 1):

                empty_space6 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_cr_ratio = Label(sub_lr, text="Your Current Ratio is "+ str(lr_current_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

                empty_space14 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_ch_ratio = Label(sub_lr, text="Your Cash Ratio is "+ str(lr_cash_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_cr_ratio == 0) and (check_q_ratio == 1) and (check_ch_ratio == 1):

                empty_space11 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_q_ratio = Label(sub_lr, text="Your Quick Ratio is "+ str(lr_quick_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

                empty_space15 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_ch_ratio = Label(sub_lr, text="Your Cash Ratio is "+ str(lr_cash_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if (check_cr_ratio == 1) and (check_q_ratio == 1) and (check_ch_ratio == 1):

                empty_space7 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_cr_ratio = Label(sub_lr, text="Your Current Ratio is "+ str(lr_current_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

                empty_space12 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_q_ratio = Label(sub_lr, text="Your Quick Ratio is "+ str(lr_quick_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

                empty_space116 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_ch_ratio = Label(sub_lr, text="Your Cash Ratio is "+ str(lr_cash_ratio),bg="#C9F7F9",font=("Arial", 10) ).pack()

        empty_space2 = Label(sub_lr, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        calculate_lr = Button(sub_lr, text="Calculate", command=calc_lr, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack()

        sublr_close_button = Button(sub_lr, text="Close Menu", command=sub_lr.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack(anchor="e")

    def opensub_lr2():
        sub_lr2 = Toplevel()
        sub_lr2.config(bg="#C9F7F9")
        sub_lr2.title("Leverage Ratios")
        sub_lr2.iconbitmap("UOL.ico")
        sub_lr2.geometry("550x600")

        lr2lbl1 = Label(sub_lr2, text= "Please select what you want to calculate", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

        lr2var1 = IntVar()

        check_debter = Checkbutton(sub_lr2, text="Debt-to-Equity Ratio", variable=lr2var1, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        lr2var2 = IntVar()

        check_debtcr = Checkbutton(sub_lr2, text="Debt-to-Capital Ratio", variable=lr2var2, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        total_debt_lbl = Label(sub_lr2, text="Enter Total Debt",bg="#C9F7F9",font=("Arial", 10)).pack()

        totaldebt = StringVar()
        totalequity = StringVar()

        total_debt = Entry(sub_lr2, textvariable = totaldebt,  bd=3).pack()

        total_equity_lbl = Label(sub_lr2, text="Enter Total Equity",bg="#C9F7F9",font=("Arial", 10)).pack()

        total_equity = Entry(sub_lr2, textvariable = totalequity, bd=3).pack()

        empty_space1 = Label(sub_lr2, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        def calc_lr2():

            checkdebt = int(lr2var1.get())
            checkequity = int(lr2var2.get())

            if checkdebt == 0 and checkequity == 0:

                error_label = Label(sub_lr2, text="Please select a calculation", bg="#C9F7F9",font=("Arial", 10)).pack()

                return

            tdebt = float(totaldebt.get())
            tequity = float(totalequity.get())
            debt_to_eq = tdebt / tequity
            debt_to_cap = tdebt/(tequity+tdebt)
            debt_to_eq = round(debt_to_eq, 2)
            debt_to_cap = round(debt_to_cap, 2)

            if checkdebt == 1 and checkequity == 0:
                empty_space2 = Label(sub_lr2, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_debtquity = Label(sub_lr2, text="Your Debt-to-Equity Ratio is "+ str(debt_to_eq),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if checkdebt == 0 and checkequity == 1:
                empty_space3 = Label(sub_lr2, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_debtcap = Label(sub_lr2, text="Your Debt-to-Capital Ratio is "+ str(debt_to_cap),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if  checkdebt == 1 and checkequity == 1:
                empty_space2 = Label(sub_lr2, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_debtquity = Label(sub_lr2, text="Your Debt-to-Equity Ratio is "+ str(debt_to_eq),bg="#C9F7F9",font=("Arial", 10) ).pack()
                empty_space3 = Label(sub_lr2, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_debtcap = Label(sub_lr2, text="Your Debt-to-Capital Ratio is "+ str(debt_to_cap),bg="#C9F7F9",font=("Arial", 10) ).pack()
            return

        calculate_lr2 = Button(sub_lr2, text="Calculate", command=calc_lr2, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack()

        sublr2_close_button = Button(sub_lr2, text="Close Menu", command=sub_lr2.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack(anchor="e")

    def opensub_or():
        sub_or = Toplevel()
        sub_or.config(bg="#C9F7F9")
        sub_or.title("Operating Ratios")
        sub_or.iconbitmap("UOL.ico")
        sub_or.geometry("550x600")

        orlbl1 = Label(sub_or, text= "Please select what you want to calculate", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

        orvar1 = IntVar()

        check_return_equity = Checkbutton(sub_or, text="Return on Equity Ratio", variable=orvar1, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        orvar2 = IntVar()

        check_return_assets = Checkbutton(sub_or, text="Return on Assets Ratio", variable=orvar2, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).pack()

        empty_space1 = Label(sub_or, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        net_income = StringVar()
        total_assets = StringVar()
        book_value_equity = StringVar()

        net_income_lbl = Label(sub_or, text="Enter Net Income",bg="#C9F7F9",font=("Arial", 10)).pack()

        net_income_ent = Entry(sub_or, textvariable = net_income,  bd=3).pack()

        total_assets_lbl = Label(sub_or, text="Enter Total Assets",bg="#C9F7F9",font=("Arial", 10)).pack()

        total_assets_ent = Entry(sub_or, textvariable = total_assets, bd=3).pack()

        book_value_equity_lbl = Label(sub_or, text="Enter Book Value of Equity",bg="#C9F7F9",font=("Arial", 10)).pack()

        book_value_equity_ent = Entry(sub_or, textvariable = book_value_equity, bd=3).pack()

        empty_space2 = Label(sub_or, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        def calc_or():

            checkrequity = int(orvar1.get())
            checkrassets = int(orvar2.get())

            if checkrequity == 0 and checkrassets == 0:

                error_lbl = Label(sub_or, text="Please select a calculation", bg="#C9F7F9",font=("Arial", 10)).pack()

                return

            n_come = float(net_income.get())
            t_assets = float(total_assets.get())
            bv_equity = float(book_value_equity.get())

            r_equity = n_come / bv_equity
            r_assets = n_come/t_assets

            r_equity = round(r_equity, 2)
            r_assets = round(r_assets, 2)

            if checkrequity == 1 and checkrassets == 0:
                empty_space2 = Label(sub_or, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_r_quity = Label(sub_or, text="Your Return on Equity Ratio is "+ str(r_equity),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if checkrequity == 0 and checkrassets == 1:
                empty_space3 = Label(sub_or, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_r_assets = Label(sub_or, text="Your Return on Asstes Ratio is "+ str(r_assets),bg="#C9F7F9",font=("Arial", 10) ).pack()

            if  checkrequity == 1 and checkrassets == 1:
                empty_space2 = Label(sub_or, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_r_quity = Label(sub_or, text="Your Return on Equity Ratio is "+ str(r_equity),bg="#C9F7F9",font=("Arial", 10) ).pack()
                empty_space3 = Label(sub_or, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
                calc_r_assets = Label(sub_or, text="Your Return on Assets Ratio is "+ str(r_assets),bg="#C9F7F9",font=("Arial", 10) ).pack()
            return

        calculate_or = Button(sub_or, text="Calculate", command=calc_or, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack()

        subor_close_button = Button(sub_or, text="Close Menu", command=sub_or.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack(anchor="e")


    mn1lbl1 = Label(menu1, text="Please select what type of calculation you want to do?", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

    mn1btn_pr = Button(menu1, text="Profitability Ratios", command=opensub_pr, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack()

    mn1btn_lr = Button(menu1, text="Liquidity Ratios", command=opensub_lr, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack()

    mn1btn_lr2 = Button(menu1, text="Leverage Ratios", command=opensub_lr2, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack()

    mn1btn_or = Button(menu1, text="Operating Ratios", command=opensub_or, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack()

    mn1close_button = Button(menu1, text="Close First Menu", command=menu1.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack(anchor="e")

mwlbl1 = Label(mainWin, text="The first menu will include basic financial calculations. (Profitability Ratios, Liquidity Ratios, \n Leverage Ratios and Operating Ratios)", bg="#C9F7F9", pady=20, font=("Arial", 10)).pack()

mwbtn1 = Button(mainWin, text="Open First Menu", bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20, command=openmenu1).pack()

#This is the code for second menu

def openmenu2():
    menu2 = Toplevel()
    menu2.config(bg="#C9F7F9")
    menu2.title("Menu No. 2")
    menu2.iconbitmap("UOL.ico")
    menu2.geometry("550x300")

    mn2lbl1 = Label(menu2, text="Please select what type of calculation you want to do?", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

    #This is the code for the future value menu
    def opensub_fv():

        sub_fv = Toplevel()
        sub_fv.config(bg="#C9F7F9")
        sub_fv.title("Future Value")
        sub_fv.iconbitmap("UOL.ico")
        sub_fv.geometry("550x450")

        fvlbl1 = Label(sub_fv, text= "Future Value Calculation", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

        empty_space = Label(sub_fv, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        amount_invest = StringVar()
        interest_rate = StringVar()
        num_years = StringVar()

        amount_invest_lbl = Label(sub_fv, text="Enter Amount of Investment",bg="#C9F7F9",font=("Arial", 10)).pack()

        amount_invest_ent = Entry(sub_fv, textvariable = amount_invest,  bd=3).pack()

        interest_rate_lbl = Label(sub_fv, text="Enter Interest Rate",bg="#C9F7F9",font=("Arial", 10)).pack()

        interest_rate_ent = Entry(sub_fv, textvariable = interest_rate,  bd=3).pack()

        num_years_lbl = Label(sub_fv, text="Enter Number of years",bg="#C9F7F9",font=("Arial", 10)).pack()

        num_years_ent = Entry(sub_fv, textvariable = num_years,  bd=3).pack()

        def calc_fv():
            calc_amount = float(amount_invest.get())
            calc_intrate = float(interest_rate.get())
            calc_years = float(num_years.get())
            calc_future_value = calc_amount*((1 + (calc_intrate / 100))**calc_years)
            empty_1 = Label(sub_fv, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
            result_fv = Label(sub_fv, text="Your Future Value is "+ str(calc_future_value),bg="#C9F7F9",font=("Arial", 10) ).pack()

        empty_space2 = Label(sub_fv, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        calculate_fv = Button(sub_fv, text="Calculate", command=calc_fv, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack()

        subfv_close_button = Button(sub_fv, text="Close Menu", command=sub_fv.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack(anchor="e")

    #This is the code for the present value menu
    def opensub_pv():

        sub_pv = Toplevel()
        sub_pv.config(bg="#C9F7F9")
        sub_pv.title("Present Value")
        sub_pv.iconbitmap("UOL.ico")
        sub_pv.geometry("550x450")

        pvlbl1 = Label(sub_pv, text= "Present Value Calculation", bg="#C9F7F9", padx=5, pady=15, font=("Arial", 10)).pack()

        empty_space = Label(sub_pv, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        amount_invest = StringVar()
        interest_rate = StringVar()
        num_years = StringVar()

        amount_invest_lbl = Label(sub_pv, text="Enter Amount of Investment",bg="#C9F7F9",font=("Arial", 10)).pack()

        amount_invest_ent = Entry(sub_pv, textvariable = amount_invest,  bd=3).pack()

        interest_rate_lbl = Label(sub_pv, text="Enter Interest Rate",bg="#C9F7F9",font=("Arial", 10)).pack()

        interest_rate_ent = Entry(sub_pv, textvariable = interest_rate,  bd=3).pack()

        num_years_lbl = Label(sub_pv, text="Enter Number of years",bg="#C9F7F9",font=("Arial", 10)).pack()

        num_years_ent = Entry(sub_pv, textvariable = num_years,  bd=3).pack()

        def calc_pv():
            calc_amount = float(amount_invest.get())
            calc_intrate = float(interest_rate.get())
            calc_years = float(num_years.get())
            calc_present_value = calc_amount / ((1 + (calc_intrate/100))**calc_years)
            calc_present_value = round(calc_present_value, 2)

            empty_1 = Label(sub_pv, text="", bg="#C9F7F9", font=("Arial", 1)).pack()
            result_pv = Label(sub_pv, text="Your Present Value is "+ str(calc_present_value),bg="#C9F7F9",font=("Arial", 10) ).pack()

        empty_space2 = Label(sub_pv, text="", bg="#C9F7F9", font=("Arial", 1)).pack()

        calculate_pv = Button(sub_pv, text="Calculate", command=calc_pv, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack()

        subpv_close_button = Button(sub_pv, text="Close Menu", command=sub_pv.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).pack(anchor="e")

    mn2btn_fv = Button(menu2, text="Future Value", command=opensub_fv, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack()

    mn2btn_pv = Button(menu2, text="Present Value", command=opensub_pv, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack()

    mn2close_button = Button(menu2, text="Close Second Menu", command=menu2.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=10, height=2, width=20).pack(anchor="e")


mwlbl2 = Label(mainWin, text="The second menu will include basic financial calculations related to the future value and present \n value of investments.", bg="#C9F7F9", pady=20, font=("Arial", 10)).pack()

mwbtn2 = Button(mainWin, text="Open Second Menu", font=("Arial",8), bg="#C1FCE2", bd=3, pady=10, height=2, width=20, command=openmenu2).pack()

#This is the code for third menu

def openmenu3():
    menu3 = Toplevel()
    menu3.config(bg="#C9F7F9")
    menu3.title("Menu No. 3")
    menu3.iconbitmap("UOL.ico")
    menu3.geometry("700x600")


    mn3lbl1 = Label(menu3, text="    Please select what type of calculation you want to do?", bg="#C9F7F9", pady=20, font=("Arial", 10)).grid(row=0,column=0, sticky="e")

    npv_var = IntVar()
    irr_var = IntVar()
    pp_var = IntVar()

    check_npv_box = Checkbutton(menu3, text="Net Present Value", variable=npv_var, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).grid(row=1,column=0, sticky="e")

    check_irr_box = Checkbutton(menu3, text="Internal Rate of Return", variable=irr_var, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).grid(row=1,column=1, sticky="e")

    check_pp_box = Checkbutton(menu3, text="Payback Period", variable=pp_var, bd=3, bg="#C9F7F9", font=("Arial", 10), onvalue=1, offvalue=0).grid(row=1,column=2, sticky="e")

    initial_invest = StringVar()

    cash_out_1 = StringVar()
    cash_out_2 = StringVar()
    cash_out_3 = StringVar()
    cash_out_4 = StringVar()
    cash_out_5 = StringVar()

    cash_in_1 = StringVar()
    cash_in_2 = StringVar()
    cash_in_3 = StringVar()
    cash_in_4 = StringVar()
    cash_in_5 = StringVar()

    discount_rate = StringVar()

    initial_invest_lbl = Label(menu3, text="Enter Initial Investment",bg="#C9F7F9",font=("Arial", 10)).grid(row=3,column=0, sticky="e")

    initial_invest_ent = Entry(menu3, textvariable = initial_invest,  bd=3).grid(row=3,column=1, sticky="e")

    cash_out_1_lbl = Label(menu3, text="Enter Year 1 Cash Outflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=4,column=0, sticky="e")

    cash_out_1_ent = Entry(menu3, textvariable = cash_out_1,  bd=3).grid(row=4,column=1, sticky="e")

    cash_out_2_lbl = Label(menu3, text="Enter Year 2 Cash Outflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=5,column=0, sticky="e")

    cash_out_2_ent = Entry(menu3, textvariable = cash_out_2,  bd=3).grid(row=5,column=1, sticky="e")

    cash_out_3_lbl = Label(menu3, text="Enter Year 3 Cash Outflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=6,column=0, sticky="e")

    cash_out_3_ent = Entry(menu3, textvariable = cash_out_3,  bd=3).grid(row=6,column=1, sticky="e")

    cash_out_4_lbl = Label(menu3, text="Enter Year 4 Cash Outflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=7,column=0, sticky="e")

    cash_out_4_ent = Entry(menu3, textvariable = cash_out_4,  bd=3).grid(row=7,column=1, sticky="e")

    cash_out_5_lbl = Label(menu3, text="Enter Year 5 Cash Outflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=8,column=0, sticky="e")

    cash_out_5_ent = Entry(menu3, textvariable = cash_out_5,  bd=3).grid(row=8,column=1, sticky="e")

    cash_in_1_lbl = Label(menu3, text="Enter Year 1 Cash Inflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=9,column=0, sticky="e")

    cash_in_1_ent = Entry(menu3, textvariable = cash_in_1,  bd=3).grid(row=9,column=1, sticky="e")

    cash_in_2_lbl = Label(menu3, text="Enter Year 2 Cash Inflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=10,column=0, sticky="e")

    cash_in_2_ent = Entry(menu3, textvariable = cash_in_2,  bd=3).grid(row=10,column=1, sticky="e")

    cash_in_3_lbl = Label(menu3, text="Enter Year 3 Cash Inflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=11,column=0, sticky="e")

    cash_in_3_ent = Entry(menu3, textvariable = cash_in_3,  bd=3).grid(row=11,column=1, sticky="e")

    cash_in_4_lbl = Label(menu3, text="Enter Year 4 Cash Inflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=12,column=0, sticky="e")

    cash_in_4_ent = Entry(menu3, textvariable = cash_in_4,  bd=3).grid(row=12,column=1, sticky="e")

    cash_in_5_lbl = Label(menu3, text="Enter Year 5 Cash Inflow",bg="#C9F7F9",font=("Arial", 10)).grid(row=13,column=0, sticky="e")

    cash_in_5_ent = Entry(menu3, textvariable = cash_in_5,  bd=3).grid(row=13,column=1, sticky="e")

    discount_rate_lbl = Label(menu3, text="Enter Discount Rate",bg="#C9F7F9",font=("Arial", 10)).grid(row=14,column=0, sticky="e")

    discount_rate_ent = Entry(menu3, textvariable = discount_rate,  bd=3).grid(row=14,column=1, sticky="e")

    def calc_mn3():

        check_npv = int(npv_var.get())
        check_irr = int(irr_var.get())
        check_pp = int(pp_var.get())

        if (check_npv == 0) and (check_irr == 0) and (check_pp == 0):

            error_label = Label(menu3, text="Please select a calculation", bg="#C9F7F9",font=("Arial", 10)).grid(row=16, column=1)

            return

        init_invest = float(initial_invest.get())

        cashout_1 = float(cash_out_1.get())
        cashout_2 = float(cash_out_2.get())
        cashout_3 = float(cash_out_3.get())
        cashout_4 = float(cash_out_4.get())
        cashout_5 = float(cash_out_5.get())

        cashin_1 = float(cash_in_1.get())
        cashin_2 = float(cash_in_2.get())
        cashin_3 = float(cash_in_3.get())
        cashin_4 = float(cash_in_4.get())
        cashin_5 = float(cash_in_5.get())

        disc_rate = float(discount_rate.get())

        cashflow1 = cashin_1 - cashout_1
        cashflow2 = cashin_2 - cashout_2
        cashflow3 = cashin_3 - cashout_3
        cashflow4 = cashin_4 - cashout_4
        cashflow5 = cashin_5 - cashout_5

        total_cashflow = cashflow1 + cashflow2 + cashflow3 + cashflow4 + cashflow5

        year0 = init_invest / ((1 + (disc_rate / 100))**0)
        year1 = cashflow1 / ((1 + (disc_rate / 100))**1)
        year2 = cashflow2 / ((1 + (disc_rate / 100))**2)
        year3 = cashflow3 / ((1 + (disc_rate / 100))**3)
        year4 = cashflow4 / ((1 + (disc_rate / 100))**4)
        year5 = cashflow5 / ((1 + (disc_rate / 100))**5)

        calc_npv = (year1 + year2 + year3 + year4 + year5) - year0

        calc_npv = round(calc_npv,2)

        neg_init_invest = - init_invest

        cashflow_list = [neg_init_invest, cashflow1, cashflow2, cashflow3, cashflow4, cashflow5]

        calc_irr = round(npf.irr(cashflow_list),4);

        irr = "{:.0%}".format(calc_irr)

        calc_pp = init_invest / total_cashflow
        calc_pp = round(calc_pp, 2)

        if (check_npv == 1) and (check_irr == 0) and (check_pp == 0):

            result_npv = Label(menu3, text="Net Present Value is "+ str(calc_npv),bg="#C9F7F9",font=("Arial", 10) ).grid(row=17, column=1)

        if (check_npv == 0) and (check_irr == 1) and (check_pp == 0):

            result_irr = Label(menu3, text="Internal Rate of Return is "+ str(irr),bg="#C9F7F9",font=("Arial", 10) ).grid(row=18, column=1)

        if (check_npv == 0) and (check_irr == 0) and (check_pp == 1):

            result_pp = Label(menu3, text="Payback Period "+ str(calc_pp) + " Years",bg="#C9F7F9",font=("Arial", 10) ).grid(row=19, column=1)

        if (check_npv == 1) and (check_irr == 1) and (check_pp == 0):
            result_npv = Label(menu3, text="Net Present Value is "+ str(calc_npv),bg="#C9F7F9",font=("Arial", 10) ).grid(row=17, column=1)

            result_irr = Label(menu3, text="Internal Rate of Return is "+ str(irr),bg="#C9F7F9",font=("Arial", 10) ).grid(row=18, column=1)

        if (check_npv == 1) and (check_irr == 0) and (check_pp == 1):
            result_npv = Label(menu3, text="Net Present Value is "+ str(calc_npv),bg="#C9F7F9",font=("Arial", 10) ).grid(row=17, column=1)

            result_pp = Label(menu3, text="Payback Period "+ str(calc_pp) + " Years",bg="#C9F7F9",font=("Arial", 10) ).grid(row=19, column=1)

        if (check_npv == 0) and (check_irr == 1) and (check_pp == 1):
            result_irr = Label(menu3, text="Internal Rate of Return is "+ str(irr),bg="#C9F7F9",font=("Arial", 10) ).grid(row=18, column=1)

            result_pp = Label(menu3, text="Payback Period "+ str(calc_pp) + " Years",bg="#C9F7F9",font=("Arial", 10) ).grid(row=19, column=1)

        if (check_npv == 1) and (check_irr == 1) and (check_pp == 1):
            result_npv = Label(menu3, text="Net Present Value is "+ str(calc_npv),bg="#C9F7F9",font=("Arial", 10) ).grid(row=17, column=1)

            result_irr = Label(menu3, text="Internal Rate of Return is "+ str(irr),bg="#C9F7F9",font=("Arial", 10) ).grid(row=18, column=1)

            result_pp = Label(menu3, text="Payback Period "+ str(calc_pp) + " Years",bg="#C9F7F9",font=("Arial", 10) ).grid(row=19, column=1)


    calculate_mn3 = Button(menu3, text="Calculate", command=calc_mn3, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=10).grid(row=15, column=2)

    mn3close_button = Button(menu3, text="Close Third Menu", command=menu3.destroy, bg="#C1FCE2", font=("Arial",8), bd =3, pady=5, height=1, width=20).grid(row=20, column=2)

mwlbl2 = Label(mainWin, text="The third menu will contain calculations for capital budgeting of a potential long-term \n investments for a 5-year project. This will include NPV(Net Present Value), IRR(Internal Rate of Return)\n and PP(Payback Period)", bg="#C9F7F9", pady=20, font=("Arial", 10)).pack()

mwbtn3 = Button(mainWin, text="Open Third Menu", font=("Arial",8), bg="#C1FCE2", bd=3, pady=10, height=2, width=20, command=openmenu3).pack()

program_close_btn = Button(mainWin, text="Close Program", command=mainWin.destroy, bd=3, bg="#C1FCE2", padx=10, pady=10, height=2, width=20).pack(anchor="e")

#Properties of the main Main Window

mainWin.config(bg="#C9F7F9")
mainWin.iconbitmap("UOL.ico")
mainWin.geometry("650x540")
mainWin.mainloop()
