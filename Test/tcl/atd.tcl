#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  Oct 09, 2024 03:36:56 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
    untitled1_jpg "../Users/RAJ KISHORE/Desktop/pic/Untitled1.jpg" 
}
vTcl:create_project_images $image_list   ;# In image.tcl

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) white
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
set vTcl(project_theme) default



proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu $top.m58 -background #dbe6ff -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 1280x657+340+90
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1284 701
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    set toptitle "Toplevel 0"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "stu_atd" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    message "$top.mes47" \
        -background #dbe6ff \
        -font "-family {Sitka Display} -size 48 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "ATTENDENCE" -width 427 
    vTcl:DefineAlias "$top.mes47" "atd" vTcl:WidgetProc "stu_atd" 1
    menu "$top.m58" \
        -activebackground #d9d9d9 -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    message "$top.mes48" \
        -background #dbe6ff \
        -font "-family {@Yu Gothic UI Semibold} -size 20 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Total -" -width 97 
    vTcl:DefineAlias "$top.mes48" "total" vTcl:WidgetProc "stu_atd" 1
    message "$top.mes50" \
        -background #dbe6ff \
        -font "-family {@Yu Gothic UI Semibold} -size 20 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Present -" -width 116 
    vTcl:DefineAlias "$top.mes50" "pst" vTcl:WidgetProc "stu_atd" 1
    text "$top.tex57" \
        -background #f2f6fe -font "-family {Segoe UI} -size 9" \
        -foreground black -height 34 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 85 \
        -wrap word 
    $top.tex57 configure -font "TkTextFont"
    $top.tex57 insert end text
    vTcl:DefineAlias "$top.tex57" "total_opt" vTcl:WidgetProc "stu_atd" 1
    text "$top.tex56" \
        -background #f2f6fe -font "-family {Segoe UI} -size 9" \
        -foreground black -height 34 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 85 \
        -wrap word 
    $top.tex56 configure -font "TkTextFont"
    $top.tex56 insert end text
    vTcl:DefineAlias "$top.tex56" "pst_opt" vTcl:WidgetProc "stu_atd" 1
    message "$top.mes52" \
        -background #dbe6ff \
        -font "-family {@Yu Gothic UI Semibold} -size 20 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Absent -" -width 126 
    vTcl:DefineAlias "$top.mes52" "abst" vTcl:WidgetProc "stu_atd" 1
    message "$top.mes53" \
        -background #dbe6ff \
        -font "-family {@Yu Gothic UI Semibold} -size 36 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Percent -" -width 235 
    vTcl:DefineAlias "$top.mes53" "per" vTcl:WidgetProc "stu_atd" 1
    button "$top.but59" \
        -activebackground #d9d9d9 -activeforeground black -background #d9d9d9 \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI Semibold} -size 11 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -text "BACK" 
    vTcl:DefineAlias "$top.but59" "Button1" vTcl:WidgetProc "stu_atd" 1
    text "$top.tex55" \
        -background #f2f6fe -font "-family {Segoe UI} -size 9" \
        -foreground black -height 34 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 85 \
        -wrap word 
    $top.tex55 configure -font "TkTextFont"
    $top.tex55 insert end text
    vTcl:DefineAlias "$top.tex55" "abst_opt" vTcl:WidgetProc "stu_atd" 1
    text "$top.tex54" \
        -background #f2f6fe -font "-family {Segoe UI} -size 9" \
        -foreground black -height 44 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 154 \
        -wrap word 
    $top.tex54 configure -font "TkTextFont"
    $top.tex54 insert end text
    vTcl:DefineAlias "$top.tex54" "per_opt" vTcl:WidgetProc "stu_atd" 1
    label "$top.lab61" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground black \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -image untitled1_jpg 
    vTcl:DefineAlias "$top.lab61" "Label1" vTcl:WidgetProc "stu_atd" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.mes47 \
        -in $top -x 0 -relx 0.078 -y 0 -rely 0.167 -width 0 -relwidth 0.334 \
        -height 0 -relheight 0.085 -anchor nw -bordermode ignore 
    place $top.mes48 \
        -in $top -x 0 -relx 0.117 -y 0 -rely 0.426 -width 0 -relwidth 0.076 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.mes50 \
        -in $top -x 0 -relx 0.102 -y 0 -rely 0.502 -width 0 -relwidth 0.091 \
        -height 0 -relheight 0.059 -anchor nw -bordermode ignore 
    place $top.tex57 \
        -in $top -x 0 -relx 0.211 -y 0 -rely 0.426 -width 0 -relwidth 0.066 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.tex56 \
        -in $top -x 0 -relx 0.211 -y 0 -rely 0.502 -width 0 -relwidth 0.066 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.mes52 \
        -in $top -x 0 -relx 0.102 -y 0 -rely 0.578 -width 0 -relwidth 0.098 \
        -height 0 -relheight 0.058 -anchor nw -bordermode ignore 
    place $top.mes53 \
        -in $top -x 0 -relx 0.086 -y 0 -rely 0.7 -width 0 -relwidth 0.184 \
        -height 0 -relheight 0.088 -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 0 -relx 0.82 -y 0 -rely 0.868 -width 97 -relwidth 0 \
        -height 36 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tex55 \
        -in $top -x 0 -relx 0.211 -y 0 -rely 0.578 -width 0 -relwidth 0.066 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.tex54 \
        -in $top -x 0 -relx 0.281 -y 0 -rely 0.715 -width 0 -relwidth 0.12 \
        -height 0 -relheight 0.067 -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 0 -relx 0.555 -y 0 -rely 0.183 -width 0 -relwidth 0.264 \
        -height 0 -relheight 0.519 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

