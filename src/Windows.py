from tkinter import *
from Stochastic import *
from tkinter.messagebox import *
from _tkinter import TclError

class Windows:
    def __init__(s, m):

        f1 = LabelFrame(m, text="Banking Queueing System", font=('Roboto', 20), fg="#9D0101")
        f1.grid(pady=20, row=0,  padx=20, column=0, rowspan=2)

        f2 = LabelFrame(m, text="Customer Inputs", font=('Roboto', 10), fg="#9D0101")
        f2.grid(pady=10, row=0,  padx=10, column=1,  columnspan=4)

        f3 = LabelFrame(m, text="Output", font=('Roboto', 10), fg="#9D0101")
        f3.grid(pady=10, row=1,  padx=10, column=1)

        fr2 = Frame(f2)
        fr2.grid(pady=5, row=0, padx=5, column=1, sticky=W)

        fr1 = Frame(f2)
        fr1.grid(pady=5, row=0, padx=5, column=0, sticky=W)

        fr6 = Frame(f3)
        fr6.grid(pady=5, row=0, padx=10, column=1)

        try:
            s.Cali = PhotoImage(file="../images/calculate.png")

            s.MM1i = PhotoImage(file="../images/m-m-1.png")
            s.MM1Ni = PhotoImage(file="../images/m-m-k.png")
            s.MMSi = PhotoImage(file="../images/m-m-c.png")
            s.MMSNi = PhotoImage(file="../images/m-m-c-k.png")
        except TclError:
            s.Cali = PhotoImage(file="./images/calculate.png")

            s.MM1i = PhotoImage(file="./images/m-m-1.png")
            s.MM1Ni = PhotoImage(file="./images/m-m-k.png")
            s.MMSi = PhotoImage(file="./images/m-m-c.png")
            s.MMSNi = PhotoImage(file="./images/m-m-c-k.png")


        s.Cal = Button(fr6, image=s.Cali, command=s.radio_event, borderwidth=0)
        s.Cal.grid(pady=3, padx=18, row=0, column=0, sticky=W)

        s.rad_values = IntVar()
        
        s.MM1 = Radiobutton(f1, image=s.MM1i, value=2, borderwidth=0, variable=s.rad_values, command=s.rad_mm1)
        s.MM1.grid(pady=0, row=0,  padx=10, column=1, sticky=W)

        s.MM1N = Radiobutton(f1, image=s.MM1Ni, value=3, borderwidth=0, variable=s.rad_values, command=s.rad_mm1n)
        s.MM1N.grid(pady=5, row=1,  padx=10, column=1, sticky=W)

        s.MMS = Radiobutton(f1, image=s.MMSi, value=4, borderwidth=0, variable=s.rad_values, command=s.rad_mms)
        s.MMS.grid(pady=0, row=2,  padx=10, column=1, sticky=W)

        s.MMSN = Radiobutton(f1, image=s.MMSNi, value=5, borderwidth=0, variable=s.rad_values, command=s.rad_mmsn)
        s.MMSN.grid(pady=5, row=3,  padx=10, column=1, sticky=W)

        s.__lambda = Label(fr1, text="Arrival rate per Sec(λ):", font=('Roboto', 18))
        s.__lambda.grid(pady=0, row=0,  padx=5, column=0, sticky=W)

        s.__miu = Label(fr1, text="Service rate per Sec(μ):", font=('Roboto', 18))
        s.__miu.grid(pady=5, row=1, padx=5, column=0, sticky=W)

        s.__k = Label(fr1, text="Total Bank Queue Capacity(N):", font=('Roboto', 18))
        s.__k.grid(padx=5, row=2, sticky=W, column=0,  pady=0)

        s.__c = Label(fr1, text="Number of Employee(S):", font=('Roboto', 18))
        s.__c.grid(row=3, pady=5,  column=0, sticky=W, padx=5)

        s.__elamda = Entry(fr2, bd=2, font=('Roboto', 10))
        s.__elamda.grid(column=1, row=0, pady=5, sticky=W,  padx=5)

        s.__emiu = Entry(fr2, bd=2, font=('Roboto', 10), justify=LEFT)
        s.__emiu.grid(column=1, row=1, pady=5, sticky=W, padx=5)

        s.__eN = Entry(fr2, bd=2, font=('Roboto', 10))
        s.__eN.grid(column=1, row=2, pady=5, sticky=W, padx=5)

        s.__eS = Entry(fr2, bd=2, font=('Roboto', 10))
        s.__eS.grid(column=1, row=3, pady=5, sticky=W, padx=5)

    @staticmethod
    def rad_dd1k(s):
        s.__eM.configure(state="normal", text="0")

    def rad_mm1(s):
        s.__elamda.configure(state="normal")
        s.__emiu.configure(state="normal")
        s.__eN.configure(state="disabled")
        s.__eS.configure(state="disabled")

    def rad_mms(s):
        s.__elamda.configure(state="normal")
        s.__emiu.configure(state="normal")
        s.__eN.configure(state="disabled")
        s.__eS.configure(state="normal")

    def rad_mm1n(s):
        s.__elamda.configure(state="normal")
        s.__emiu.configure(state="normal")
        s.__eN.configure(state="normal")
        s.__eS.configure(state="disabled")

    def rad_mmsn(s):
        s.__elamda.configure(state="normal")
        s.__emiu.configure(state="normal")
        s.__eN.configure(state="normal")
        s.__eS.configure(state="normal") 

    def radio_event(s):
        radio_selected = s.rad_values.get()
      
        if radio_selected == 2:
            try:
                mm1 = MM1(s.__elamda.get(), s.__emiu.get())

                try:
                    customerl = mm1.customerl()
                    customerlq = mm1.customerlq()
                    timeW = mm1.timeW()
                    timeWq = mm1.timeWq()
                    rho = mm1.get_rho()
                except ZeroDivisionError as zd:
                    showerror(title="You have made an Error!", message=f"{zd}!")
                except Exception as e:
                    showerror(title="You have made an Error!", message=f"{e}!")
                else:
                    answer = Tk()
                    answer.title("M/M/1")

                    lf_l = LabelFrame(answer, text="Average Customers in Banking System", font=('Roboto', 10), fg="#b34700")
                    lf_l.grid(padx=10, row=0, pady=10, column=0)

                    cap_l_le = Label(lf_l, text="L =", font=('Roboto', 18), fg="#b34700")
                    cap_l_le.grid(padx=10, row=0, pady=5, column=0)

                    capital_l_right = Label(lf_l, text=f"{customerl} Customers", font=('Roboto', 18), fg="#b34700")
                    capital_l_right.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_lq = LabelFrame(answer, text="Average Customers in Banking System Queue", font=('Roboto', 10), fg="#000000")
                    lf_lq.grid(column=0, row=1, padx=10, sticky=W, pady=10)

                    customerlq_left = Label(lf_lq, text="Lq =", font=('Roboto', 18), fg="#000000")
                    customerlq_left.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    customerlq_right = Label(lf_lq, text=f"{customerlq} Customers", font=('Roboto', 18), fg="#000000")
                    customerlq_right.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_w = LabelFrame(answer, text="Average Time Spent in Banking System", font=('Roboto', 10), fg="#900d90")
                    lf_w.grid(column=0, row=2, padx=10, sticky=W, pady=10)

                    cap_w_l = Label(lf_w, text="W =", font=('Roboto', 18), fg="#900d90")
                    cap_w_l.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    cap_w_r = Label(lf_w, text=f"{timeW} Seconds", font=('Roboto', 18), fg="#900d90")
                    cap_w_r.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Roboto', 10), fg="#000000")
                    lf_wq.grid(column=0, row=3, padx=10, sticky=W, pady=10)

                    cap_Wq_l = Label(lf_wq, text="Wq =", font=('Roboto', 18), fg="#000000")
                    cap_Wq_l.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    cap_Wq_r = Label(lf_wq, text=f"{timeWq} Seconds", font=('Roboto', 18), fg="#000000")
                    cap_Wq_r.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_ro = LabelFrame(answer, text="Utilization Factor", font=('Roboto', 10), fg="#000000")
                    lf_ro.grid(column=0, row=4, padx=10, sticky=W, pady=10)

                    cap_ro_left = Label(lf_ro, text="ρ =", font=('Roboto', 18), fg="#000000")
                    cap_ro_left.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    cap_ro_right = Label(lf_ro, text=f"{rho}", font=('Roboto', 18), fg="#000000")
                    cap_ro_right.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    answer.mainloop()
                    del mm1

            except SyntaxError:
                showerror(title="You have made an Error!", message="Please! enter a suitable value for λ and μ.")
            except ZeroDivisionError as zd:
                showerror(title="You have made an Error!", message=f"{zd}!")
            except Exception as e:
                showerror(title="You have made an Error!", message=f"{e}!")

        elif radio_selected == 3:
            try:
                mm1n = MM1N(s.__elamda.get(), s.__emiu.get(), s.__eN.get())

                try:
                    timeW = mm1n.timeW()
                    timeWq = mm1n.timeWq()
                    customerl = mm1n.customerl()
                    customerlq = mm1n.customerlq()
                    rho = mm1n.get_rho()
                except ZeroDivisionError as zd:
                    showerror(title="You have made an Error!", message=f"{zd}!")
                except Exception as e:
                    showerror(title="You have made an Error!", message=f"{e}!")
                else:
                    answer = Tk()
                    answer.title("M/M/1/K")

                    lf_l = LabelFrame(answer, text="Average Customers in Banking System", font=('Roboto', 10), fg="#b34700")
                    lf_l.grid(column=0, row=0, padx=10, sticky=W, pady=10)

                    cap_l_le = Label(lf_l, text="L =", font=('Roboto', 18), fg="#b34700")
                    cap_l_le.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    capital_l_right = Label(lf_l, text=f"{customerl} Customers", font=('Roboto', 18), fg="#b34700")
                    capital_l_right.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_lq = LabelFrame(answer, text="Average Customers in Banking System Queue", font=('Roboto', 10), fg="#000000")
                    lf_lq.grid(column=0, row=1, padx=10, sticky=W, pady=10)

                    customerlq_left = Label(lf_lq, text="Lq =", font=('Roboto', 18), fg="#000000")
                    customerlq_left.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    customerlq_right = Label(lf_lq, text=f"{customerlq} Customers", font=('Roboto', 18), fg="#000000")
                    customerlq_right.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_w = LabelFrame(answer, text="Average Time Spent in Banking System", font=('Roboto', 10), fg="#900d90")
                    lf_w.grid(column=0, row=2, padx=10, sticky=W, pady=10)

                    cap_w_l = Label(lf_w, text="W =", font=('Roboto', 18), fg="#900d90")
                    cap_w_l.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    cap_w_r = Label(lf_w, text=f"{timeW} Seconds", font=('Roboto', 18), fg="#900d90")
                    cap_w_r.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Roboto', 10), fg="#000000")
                    lf_wq.grid(column=0, row=3, padx=10, sticky=W, pady=10)

                    cap_Wq_l = Label(lf_wq, text="Wq =", font=('Roboto', 18), fg="#000000")
                    cap_Wq_l.grid(column=0, row=0, padx=10, sticky=W,  pady=5)

                    cap_Wq_r = Label(lf_wq, text=f"{timeWq} Seconds", font=('Roboto', 18), fg="#000000")
                    cap_Wq_r.grid(column=1, row=0, padx=10,sticky=W,  pady=5)

                    lf_ro = LabelFrame(answer, text="Utilization Factor", font=('Roboto', 10), fg="#000000")
                    lf_ro.grid(column=0, row=4, padx=10, sticky=W, pady=10)

                    cap_ro_left = Label(lf_ro, text="ρ =", font=('Roboto', 18), fg="#000000")
                    cap_ro_left.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    cap_ro_right = Label(lf_ro, text=f"{rho}", font=('Roboto', 18), fg="#000000")
                    cap_ro_right.grid(column=1, row=0, padx=10, sticky=W,  pady=5)

                    answer.mainloop()
                    del mm1n

            except SyntaxError:
                showerror(title="You have made an Error!", message="Please! enter a suitable value for λ, μ and N.")
            except ZeroDivisionError as zd:
                showerror(title="You have made an Error!", message=f"{zd}!")
            except Exception as e:
                showerror(title="You have made an Error!", message=f"{e}!")

        elif radio_selected == 4:
            try:
                mms = MMS(s.__elamda.get(), s.__emiu.get(), s.__eS.get())

                try:
                    timeW = mms.timeW()
                    timeWq = mms.timeWq()
                    customerl = mms.customerl()
                    customerlq = mms.customerlq()
                    rho = mms.get_rho()
                except ZeroDivisionError as zd:
                    showerror(title="You have made an Error!", message=f"{zd}!")
                except Exception as e:
                    showerror(title="You have made an Error!", message=f"{e}!")
                else:
                    answer = Tk()
                    answer.title("M/M/C")

                    lf_l = LabelFrame(answer, text="Average Customers in Banking System", font=('Roboto', 10), fg="#b34700")
                    lf_l.grid(column=0, row=0, padx=10, sticky=W, pady=10)

                    cap_l_le = Label(lf_l, text="L =", font=('Roboto', 18), fg="#b34700")
                    cap_l_le.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    capital_l_right = Label(lf_l, text=f"{customerl} Customers", font=('Roboto', 18), fg="#b34700")
                    capital_l_right.grid(column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_lq = LabelFrame(answer, text="Average Customers in Banking System Queue", font=('Roboto', 10), fg="#000000")
                    lf_lq.grid(column=0, row=1, padx=10, sticky=W, pady=10)

                    customerlq_left = Label(lf_lq, text="Lq =", font=('Roboto', 18), fg="#000000")
                    customerlq_left.grid(column=0, row=0, padx=10,  sticky=W, pady=5)

                    customerlq_right = Label(lf_lq, text=f"{customerlq} Customers", font=('Roboto', 18), fg="#000000")
                    customerlq_right.grid(column=1, row=0, padx=10,  sticky=W, pady=5)

                    lf_w = LabelFrame(answer, text="Average Time Spent in Banking System", font=('Roboto', 10), fg="#900d90")
                    lf_w.grid(column=0, row=2, padx=10, sticky=W, pady=10)

                    cap_w_l = Label(lf_w, text="W =", font=('Roboto', 18), fg="#900d90")
                    cap_w_l.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    cap_w_r = Label(lf_w, text=f"{timeW} Seconds", font=('Roboto', 18), fg="#900d90")
                    cap_w_r.grid(column=1, row=0, padx=10, sticky=W,  pady=5)

                    lf_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Roboto', 10), fg="#000000")
                    lf_wq.grid(column=0, row=3,  padx=10, sticky=W, pady=10)

                    cap_Wq_l = Label(lf_wq, text="Wq =", font=('Roboto', 18), fg="#000000")
                    cap_Wq_l.grid(column=0, row=0, padx=10,  sticky=W, pady=5)

                    cap_Wq_r = Label(lf_wq, text=f"{timeWq} Seconds", font=('Roboto', 18), fg="#000000")
                    cap_Wq_r.grid( column=1, row=0, padx=10, sticky=W, pady=5)

                    lf_ro = LabelFrame(answer, text="Utilization Factor", font=('Roboto', 10), fg="#000000")
                    lf_ro.grid(column=0, row=4, padx=10,  sticky=W, pady=10)

                    cap_ro_left = Label(lf_ro, text="ρ =", font=('Roboto', 18), fg="#000000")
                    cap_ro_left.grid(column=0, row=0, padx=10, sticky=W,  pady=5)

                    cap_ro_right = Label(lf_ro, text=f"{rho}", font=('Roboto', 18), fg="#000000")
                    cap_ro_right.grid(column=1, row=0, padx=10, sticky=W,  pady=5)

                    answer.mainloop()
                    del mms

            except SyntaxError:
                showerror(title="You have made an Error!", message="Please! enter a suitable value for λ, μ and S.")
            except ZeroDivisionError as zd:
                showerror(title="You have made an Error!", message=f"{zd}!")
            except Exception as e:
                showerror(title="You have made an Error!", message=f"{e}!")

        elif radio_selected == 5:
            try:
                mmsn = MMSN(s.__elamda.get(), s.__emiu.get(), s.__eS.get(), s.__eN.get())

                try:
                    timeW = mmsn.timeW()
                    timeWq = mmsn.timeWq()
                    customerl = mmsn.customerl()
                    customerlq = mmsn.customerlq()
                    rho = mmsn.get_rho()
                except ZeroDivisionError as zd:
                    showerror(title="You have made an Error!", message=f"{zd}!")
                except Exception as e:
                    showerror(title="You have made an Error!", message=f"{e}!")
                else:
                    answer = Tk()
                    answer.title("M/M/C/K")

                    lf_l = LabelFrame(answer, text="Average Customers in Banking System", font=('Roboto', 10), fg="#b34700")
                    lf_l.grid(column=0, row=0, padx=10, sticky=W,  pady=10)

                    cap_l_le = Label(lf_l, text="L =", font=('Roboto', 18), fg="#b34700")
                    cap_l_le.grid(column=0, row=0, padx=10, sticky=W, pady=5)

                    capital_l_right = Label(lf_l, text=f"{customerl} Customers", font=('Roboto', 18), fg="#b34700")
                    capital_l_right.grid(column=1, row=0, padx=10,  sticky=W, pady=5)

                    lf_lq = LabelFrame(answer, text="Average Customers in Banking System Queue", font=('Roboto', 10), fg="#000000")
                    lf_lq.grid(column=0, row=1, padx=10, sticky=W,  pady=10)

                    customerlq_left = Label(lf_lq, text="Lq =", font=('Roboto', 18), fg="#000000")
                    customerlq_left.grid(column=0, row=0, padx=10, sticky=W,  pady=5)

                    customerlq_right = Label(lf_lq, text=f"{customerlq} Customers", font=('Roboto', 18), fg="#000000")
                    customerlq_right.grid(column=1, row=0,  padx=10, sticky=W, pady=5)

                    lf_w = LabelFrame(answer, text="Average Time Spent in Banking System", font=('Roboto', 10), fg="#900d90")
                    lf_w.grid(column=0, row=2,  padx=10, sticky=W, pady=10)

                    cap_w_l = Label(lf_w, text="W =", font=('Roboto', 18), fg="#900d90")
                    cap_w_l.grid(column=0, row=0, padx=10, sticky=W,  pady=5)

                    cap_w_r = Label(lf_w, text=f"{timeW} Seconds", font=('Roboto', 18), fg="#900d90")
                    cap_w_r.grid(column=1, row=0, padx=10, sticky=W,  pady=5)

                    lf_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Roboto', 10), fg="#000000")
                    lf_wq.grid(column=0, row=3, padx=10,  sticky=W, pady=10)

                    cap_Wq_l = Label(lf_wq, text="Wq =", font=('Roboto', 18), fg="#000000")
                    cap_Wq_l.grid( column=0, row=0, padx=10, sticky=W,  pady=5)

                    cap_Wq_r = Label(lf_wq, text=f"{timeWq} Seconds", font=('Roboto', 18), fg="#000000")
                    cap_Wq_r.grid(column=1, row=0, padx=10,  sticky=W, pady=5)

                    lf_ro = LabelFrame(answer, text="Utilization Factor", font=('Roboto', 10), fg="#000000")
                    lf_ro.grid(column=0, row=4, padx=10, sticky=W, pady=10)

                    cap_ro_left = Label(lf_ro, text="ρ =", font=('Roboto', 18), fg="#000000")
                    cap_ro_left.grid(column=0, row=0, padx=10, sticky=W,  pady=5)

                    cap_ro_right = Label(lf_ro, text=f"{rho}", font=('Roboto', 18), fg="#000000")
                    cap_ro_right.grid(column=1, row=0, padx=10, sticky=W,  pady=5)

                    answer.mainloop()
                    del mmsn

            except SyntaxError:
                showerror(title="You have made an Error!", message="Please! enter a suitable value for λ, μ, S and N")
            except ZeroDivisionError as zd:
                showerror(title="You have made an Error!", message=f"{zd}")
            except Exception as e:
                showerror(title="You have made an Error!", message=f"{e}")

        else:
            showwarning(title="Warn!", message="Please! At first Choose a Model!")
