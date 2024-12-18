#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  Oct 08, 2024 04:57:14 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


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
set vTcl(mode) Absolute
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
        -menu $top.m64 -background #dbe6ff -highlightbackground #d9d9d9 \
        -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 1326x675+-5+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1330 727
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Time_table"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Time_table" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m64" \
        -activebackground #d9d9d9 -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    frame "$top.fra48" \
        -borderwidth 2 -relief groove -background #f2f6fe -height 486 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 906 
    vTcl:DefineAlias "$top.fra48" "Frame1" vTcl:WidgetProc "Time_table" 1
    set site_3_0 $top.fra48
    ttk::separator "$site_3_0.tSe51"
    vTcl:DefineAlias "$site_3_0.tSe51" "TSeparator1" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe51
    ttk::separator "$site_3_0.tSe55"
    vTcl:DefineAlias "$site_3_0.tSe55" "TSeparator3" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe55
    ttk::separator "$site_3_0.tSe53"
    vTcl:DefineAlias "$site_3_0.tSe53" "TSeparator1_1" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe53
    ttk::separator "$site_3_0.tSe54"
    vTcl:DefineAlias "$site_3_0.tSe54" "TSeparator2" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe54
    ttk::separator "$site_3_0.tSe58" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe58" "TSeparator6" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe58
    ttk::separator "$site_3_0.tSe57" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe57" "TSeparator5" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe57
    ttk::separator "$site_3_0.tSe56" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe56" "TSeparator4" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe56
    ttk::separator "$site_3_0.tSe59" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe59" "TSeparator7" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe59
    ttk::separator "$site_3_0.tSe60" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe60" "TSeparator8" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe60
    ttk::separator "$site_3_0.tSe62" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe62" "TSeparator10" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe62
    ttk::separator "$site_3_0.tSe61" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe61" "TSeparator9" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.tSe61
    message "$site_3_0.mes48" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "IP" -width 100 
    vTcl:DefineAlias "$site_3_0.mes48" "Message3" vTcl:WidgetProc "Time_table" 1
    vTcl:copy_lock $site_3_0.mes48
    frame "$site_3_0.fra49" \
        -borderwidth 2 -relief groove -background #f2f6fe -height 420 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 113 
    vTcl:DefineAlias "$site_3_0.fra49" "Frame2" vTcl:WidgetProc "Time_table" 1
    set site_4_0 $site_3_0.fra49
    message "$site_4_0.mes65" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "DAY-1" -width 80 
    vTcl:DefineAlias "$site_4_0.mes65" "Message2" vTcl:WidgetProc "Time_table" 1
    place $site_4_0.mes65 \
        -in $site_4_0 -x 10 -y 20 -width 80 -relwidth 0 -height 49 \
        -relheight 0 -anchor nw -bordermode ignore 
    vTcl:copy_lock $site_3_0.fra49
    message "$site_3_0.mes56" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Chemistry" -width 100 
    vTcl:DefineAlias "$site_3_0.mes56" "Message3_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    frame "$site_3_0.fra50" \
        -borderwidth 2 -relief groove -background #f2f6fe -height 75 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -width 952 
    vTcl:DefineAlias "$site_3_0.fra50" "Frame3" vTcl:WidgetProc "Time_table" 1
    set site_4_0 $site_3_0.fra50
    message "$site_4_0.mes77" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-1" -width 80 
    vTcl:DefineAlias "$site_4_0.mes77" "Message2_2_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    place $site_4_0.mes77 \
        -in $site_4_0 -x 20 -y 10 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $site_3_0.fra50
    message "$site_3_0.mes82" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Phe/
Painting" \
        -width 100 
    vTcl:DefineAlias "$site_3_0.mes82" "Message3_1_1_1_1_1_2_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes95" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Maths" -width 100 
    vTcl:DefineAlias "$site_3_0.mes95" "Message3_1_1_1_1_1_2_1_1_1_3_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes96" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "English" -width 100 
    vTcl:DefineAlias "$site_3_0.mes96" "Message3_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes103" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Library" -width 100 
    vTcl:DefineAlias "$site_3_0.mes103" "Message3_2_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes49" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Maths" -width 100 
    vTcl:DefineAlias "$site_3_0.mes49" "Message3_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes58" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "English" -width 100 
    vTcl:DefineAlias "$site_3_0.mes58" "Message3_1_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes83" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Games" -width 100 
    vTcl:DefineAlias "$site_3_0.mes83" "Message3_1_1_1_1_1_2_1_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes93" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Chemistry" -width 100 
    vTcl:DefineAlias "$site_3_0.mes93" "Message3_1_1_1_1_1_2_1_1_1_3_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes104" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Physics" -width 100 
    vTcl:DefineAlias "$site_3_0.mes104" "Message3_2_2_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes59" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Maths" -width 100 
    vTcl:DefineAlias "$site_3_0.mes59" "Message3_1_1_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes76" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Chemistry" -width 100 
    vTcl:DefineAlias "$site_3_0.mes76" "Message3_1_1_1_1_1_2_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes66" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify center -padx 1 -pady 1 \
        -text "Physics
Lab" -width 100 
    vTcl:DefineAlias "$site_3_0.mes66" "Message3_1_1_1_1_1_2_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes84" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify center -padx 1 -pady 1 \
        -text "IP
Lab" -width 100 
    vTcl:DefineAlias "$site_3_0.mes84" "Message3_1_1_1_1_1_2_1_1_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes91" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "English" -width 100 
    vTcl:DefineAlias "$site_3_0.mes91" "Message3_1_1_1_1_1_2_1_1_1_3_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes99" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -width 100 
    vTcl:DefineAlias "$site_3_0.mes99" "Message3_2_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes105" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "IP" -width 100 
    vTcl:DefineAlias "$site_3_0.mes105" "Message3_2_2_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes51" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Chemistry" -width 100 
    vTcl:DefineAlias "$site_3_0.mes51" "Message3_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes61" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "English" -width 100 
    vTcl:DefineAlias "$site_3_0.mes61" "Message3_1_1_1_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes79" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Maths" -width 100 
    vTcl:DefineAlias "$site_3_0.mes79" "Message3_1_1_1_1_1_2_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes86" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "IP" -width 100 
    vTcl:DefineAlias "$site_3_0.mes86" "Message3_1_1_1_1_1_2_1_1_1_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes100" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Library" -width 100 
    vTcl:DefineAlias "$site_3_0.mes100" "Message3_2_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes106" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Games" -width 100 
    vTcl:DefineAlias "$site_3_0.mes106" "Message3_2_1_1_1_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes90" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Physics" -width 100 
    vTcl:DefineAlias "$site_3_0.mes90" "Message3_1_1_1_1_1_2_1_1_1_3_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes53" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "English" -width 100 
    vTcl:DefineAlias "$site_3_0.mes53" "Message3_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes62" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Maths" -width 100 
    vTcl:DefineAlias "$site_3_0.mes62" "Message3_1_1_1_1_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes88" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Physics" -width 100 
    vTcl:DefineAlias "$site_3_0.mes88" "Message3_1_1_1_1_1_2_1_1_1_3_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes107" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "IP" -width 100 
    vTcl:DefineAlias "$site_3_0.mes107" "Message3_2_1_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes87" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Phe/
Painting" \
        -width 100 
    vTcl:DefineAlias "$site_3_0.mes87" "Message3_1_1_1_1_1_2_1_1_1_3" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes101" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Chemistry" -width 100 
    vTcl:DefineAlias "$site_3_0.mes101" "Message3_2_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes80" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify center -padx 1 -pady 1 \
        -text "Chemistry
Lab" -width 100 
    vTcl:DefineAlias "$site_3_0.mes80" "Message3_1_1_1_1_1_2_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes97" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify center -padx 1 -pady 1 \
        -text "IP
Lab" -width 100 
    vTcl:DefineAlias "$site_3_0.mes97" "Message3_2_1" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes63" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Physics" -width 100 
    vTcl:DefineAlias "$site_3_0.mes63" "Message3_1_1_1_1_1_2" vTcl:WidgetProc "Time_table" 1
    message "$site_3_0.mes50" \
        -background #f2f6fe -font "-family {Segoe UI} -size 16" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Physics" -width 100 
    vTcl:DefineAlias "$site_3_0.mes50" "Message3_1_1" vTcl:WidgetProc "Time_table" 1
    place $site_3_0.tSe51 \
        -in $site_3_0 -x 3 -y 151 -width 1050 -relwidth 0 -height 0 \
        -relheight 0.004 -anchor nw -bordermode ignore 
    place $site_3_0.tSe55 \
        -in $site_3_0 -x -8 -y 402 -width 1054 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe53 \
        -in $site_3_0 -x -5 -y 234 -width 1066 -relwidth 0 -height 0 \
        -relheight 0.004 -anchor nw -bordermode ignore 
    place $site_3_0.tSe54 \
        -in $site_3_0 -x -6 -y 312 -width 1054 -relwidth 0 -height 0 \
        -relheight 0.004 -anchor nw -bordermode ignore 
    place $site_3_0.tSe58 \
        -in $site_3_0 -x 452 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe57 \
        -in $site_3_0 -x 332 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe56 \
        -in $site_3_0 -x 222 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe59 \
        -in $site_3_0 -x 562 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe60 \
        -in $site_3_0 -x 682 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe62 \
        -in $site_3_0 -x 912 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe61 \
        -in $site_3_0 -x 792 -y 2 -height 480 -relheight 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes48 \
        -in $site_3_0 -x 110 -y 80 -width 100 -relwidth 0 -height 59 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra49 \
        -in $site_3_0 -x 0 -y 69 -width 96 -relwidth 0 -height 418 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes56 \
        -in $site_3_0 -x 230 -y 80 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra50 \
        -in $site_3_0 -x 94 -y 0 -width 812 -relwidth 0 -height 72 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes82 \
        -in $site_3_0 -x 460 -y 80 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes95 \
        -in $site_3_0 -x 570 -y 80 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes96 \
        -in $site_3_0 -x 690 -y 80 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes103 \
        -in $site_3_0 -x 800 -y 80 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes49 \
        -in $site_3_0 -x 110 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes58 \
        -in $site_3_0 -x 230 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes83 \
        -in $site_3_0 -x 460 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes93 \
        -in $site_3_0 -x 570 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes104 \
        -in $site_3_0 -x 800 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes59 \
        -in $site_3_0 -x 230 -y 240 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes76 \
        -in $site_3_0 -x 340 -y 250 -width 100 -relwidth 0 -height 49 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes66 \
        -in $site_3_0 -x 340 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes84 \
        -in $site_3_0 -x 460 -y 240 -width 100 -relwidth 0 -height 59 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes91 \
        -in $site_3_0 -x 580 -y 250 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes99 \
        -in $site_3_0 -x 690 -y 240 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes105 \
        -in $site_3_0 -x 800 -y 240 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes51 \
        -in $site_3_0 -x 110 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes61 \
        -in $site_3_0 -x 230 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes79 \
        -in $site_3_0 -x 340 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes86 \
        -in $site_3_0 -x 460 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes100 \
        -in $site_3_0 -x 690 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes106 \
        -in $site_3_0 -x 800 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes90 \
        -in $site_3_0 -x 570 -y 330 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes53 \
        -in $site_3_0 -x 110 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes62 \
        -in $site_3_0 -x 230 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes88 \
        -in $site_3_0 -x 570 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes107 \
        -in $site_3_0 -x 800 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes87 \
        -in $site_3_0 -x 460 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes101 \
        -in $site_3_0 -x 690 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes80 \
        -in $site_3_0 -x 340 -y 410 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes97 \
        -in $site_3_0 -x 690 -y 160 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes63 \
        -in $site_3_0 -x 340 -y 80 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes50 \
        -in $site_3_0 -x 110 -y 240 -width 100 -height 59 -anchor nw \
        -bordermode ignore 
    vTcl:copy_lock $top.fra48
    message "$top.mes68" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "DAY-3" -width 80 
    vTcl:DefineAlias "$top.mes68" "Message2_1_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes69" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "DAY-4" -width 80 
    vTcl:DefineAlias "$top.mes69" "Message2_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes70" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "DAY-5" -width 80 
    vTcl:DefineAlias "$top.mes70" "Message2_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes72" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-2" -width 80 
    vTcl:DefineAlias "$top.mes72" "Message2_2_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes73" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-3" -width 80 
    vTcl:DefineAlias "$top.mes73" "Message2_2_1_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes74" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-4" -width 80 
    vTcl:DefineAlias "$top.mes74" "Message2_2_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes75" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-5" -width 80 
    vTcl:DefineAlias "$top.mes75" "Message2_2_1_1_1_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes67" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "DAY-2" -width 80 
    vTcl:DefineAlias "$top.mes67" "Message2_1" vTcl:WidgetProc "Time_table" 1
    message "$top.mes71" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-6" -width 80 
    vTcl:DefineAlias "$top.mes71" "Message2_2" vTcl:WidgetProc "Time_table" 1
    message "$top.mes78" \
        -background #f2f6fe -font "-family {Segoe UI} -size 12" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Period-7" -width 80 
    vTcl:DefineAlias "$top.mes78" "Message2_2_2" vTcl:WidgetProc "Time_table" 1
    message "$top.mes47" \
        -background #dbe6ff \
        -font "-family {Arial Black} -size 30 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -justify center -padx 1 -pady 1 \
        -text "Time Table" -width 272 
    vTcl:DefineAlias "$top.mes47" "Message1" vTcl:WidgetProc "Time_table" 1
    button "$top.but63" \
        -activebackground #f2f6fe -activeforeground black -background #f2f6fe \
        -disabledforeground #a3a3a3 -font "-family {Segoe UI} -size 9" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -text "Back" 
    vTcl:DefineAlias "$top.but63" "Button1" vTcl:WidgetProc "Time_table" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra48 \
        -in $top -x 180 -y 120 -width 906 -relwidth 0 -height 486 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.mes68 \
        -in $top -x 190 -y 370 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes69 \
        -in $top -x 190 -y 450 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes70 \
        -in $top -x 190 -y 540 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes72 \
        -in $top -x 420 -y 130 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes73 \
        -in $top -x 530 -y 130 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes74 \
        -in $top -x 640 -y 130 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes75 \
        -in $top -x 760 -y 130 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes67 \
        -in $top -x 190 -y 290 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes71 \
        -in $top -x 870 -y 130 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes78 \
        -in $top -x 980 -y 130 -width 80 -height 49 -anchor nw \
        -bordermode ignore 
    place $top.mes47 \
        -in $top -x 160 -y 30 -width 272 -relwidth 0 -height 79 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 1120 -y 620 -width 90 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 

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

