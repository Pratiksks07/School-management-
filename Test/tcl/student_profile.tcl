#############################################################################
# Generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#  Oct 10, 2024 04:40:05 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
    bg1(1)_png "../Users/RAJ KISHORE/Downloads/bg1(1).png" 
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
        -menu $top.m47 -background #dbe6ff -highlightbackground #d9d9d9 \
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
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m47" \
        -activebackground #d9d9d9 -activeforeground black \
        -font "-family {Segoe UI} -size 9" -tearoff 0 
    text "$top.tex60" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex60 configure -font "TkTextFont"
    $top.tex60 insert end text
    vTcl:DefineAlias "$top.tex60" "Text1_1_1" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex59" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex59 configure -font "TkTextFont"
    $top.tex59 insert end text
    vTcl:DefineAlias "$top.tex59" "Text1_1" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex58" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex58 configure -font "TkTextFont"
    $top.tex58 insert end text
    vTcl:DefineAlias "$top.tex58" "Text1" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex61" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex61 configure -font "TkTextFont"
    $top.tex61 insert end text
    vTcl:DefineAlias "$top.tex61" "Text1_2" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex62" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex62 configure -font "TkTextFont"
    $top.tex62 insert end text
    vTcl:DefineAlias "$top.tex62" "Text1_2_1" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex63" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex63 configure -font "TkTextFont"
    $top.tex63 insert end text
    vTcl:DefineAlias "$top.tex63" "Text1_2_1_1" vTcl:WidgetProc "Toplevel1" 1
    button "$top.but67" \
        -activebackground #d9d9d9 -activeforeground black -background #dbe6ff \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 13 -weight bold" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 -text "BACK" 
    vTcl:DefineAlias "$top.but67" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label "$top.lab66" \
        -activebackground #d9d9d9 -activeforeground black -anchor w \
        -background #d9d9d9 -compound left -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9" -foreground #000000 \
        -highlightbackground #d9d9d9 -highlightcolor #000000 \
        -image bg1(1)_png 
    vTcl:DefineAlias "$top.lab66" "Label1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes48" \
        -background #dbe6ff \
        -font "-family {Sitka Display} -size 48 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Profile" -width 206 
    vTcl:DefineAlias "$top.mes48" "heading" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex65" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex65 configure -font "TkTextFont"
    $top.tex65 insert end text
    vTcl:DefineAlias "$top.tex65" "Text1_2_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes49" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Name :" -width 81 
    vTcl:DefineAlias "$top.mes49" "name" vTcl:WidgetProc "Toplevel1" 1
    text "$top.tex64" \
        -background white -font "-family {Segoe UI} -size 9" \
        -foreground black -height 35 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -insertbackground #000000 \
        -selectbackground #d9d9d9 -selectforeground black -width 224 \
        -wrap word 
    $top.tex64 configure -font "TkTextFont"
    $top.tex64 insert end text
    vTcl:DefineAlias "$top.tex64" "Text1_2_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes51" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Class :" -width 101 
    vTcl:DefineAlias "$top.mes51" "class" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes52" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Sec :" -width 102 
    vTcl:DefineAlias "$top.mes52" "sec" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes53" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Roll no :" -width 140 
    vTcl:DefineAlias "$top.mes53" "roll" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes54" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Adm no :" -width 140 
    vTcl:DefineAlias "$top.mes54" "adm" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes55" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Father's Name :" \
        -width 208 
    vTcl:DefineAlias "$top.mes55" "fname" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes56" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Mother's Name :" \
        -width 208 
    vTcl:DefineAlias "$top.mes56" "address" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes57" \
        -background #dbe6ff -font "-family {Arial} -size 17 -weight bold" \
        -foreground #000000 -highlightbackground #d9d9d9 \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Address :" -width 121 
    vTcl:DefineAlias "$top.mes57" "Message2_1_1_1_1_2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tex60 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.807 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.053 -anchor nw -bordermode ignore 
    place $top.tex59 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.731 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.053 -anchor nw -bordermode ignore 
    place $top.tex58 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.654 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.053 -anchor nw -bordermode ignore 
    place $top.tex61 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.578 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.tex62 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.502 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.tex63 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.426 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.but67 \
        -in $top -x 0 -relx 0.844 -y 0 -rely 0.898 -width 77 -relwidth 0 \
        -height 26 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 0 -relx 0.578 -y 0 -rely 0.183 -width 0 -relwidth 0.298 \
        -height 0 -relheight 0.536 -anchor nw -bordermode ignore 
    place $top.mes48 \
        -in $top -x 0 -relx 0.047 -y 0 -rely 0.061 -width 0 -relwidth 0.161 \
        -height 0 -relheight 0.11 -anchor nw -bordermode ignore 
    place $top.tex65 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.274 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.mes49 \
        -in $top -x 0 -relx 0.086 -y 0 -rely 0.274 -width 0 -relwidth 0.063 \
        -height 0 -relheight 0.058 -anchor nw -bordermode ignore 
    place $top.tex64 \
        -in $top -x 0 -relx 0.242 -y 0 -rely 0.35 -width 0 -relwidth 0.175 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.mes51 \
        -in $top -x 0 -relx 0.078 -y 0 -rely 0.35 -width 0 -relwidth 0.08 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.mes52 \
        -in $top -x 0 -relx 0.07 -y 0 -rely 0.411 -width 0 -relwidth 0.08 \
        -height 0 -relheight 0.075 -anchor nw -bordermode ignore 
    place $top.mes53 \
        -in $top -x 0 -relx 0.07 -y 0 -rely 0.502 -width 0 -relwidth 0.109 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.mes54 \
        -in $top -x 0 -relx 0.07 -y 0 -rely 0.578 -width 0 -relwidth 0.109 \
        -height 0 -relheight 0.059 -anchor nw -bordermode ignore 
    place $top.mes55 \
        -in $top -x 0 -relx 0.07 -y 0 -rely 0.654 -width 0 -relwidth 0.163 \
        -height 0 -relheight 0.059 -anchor nw -bordermode ignore 
    place $top.mes56 \
        -in $top -x 0 -relx 0.07 -y 0 -rely 0.731 -width 0 -relwidth 0.163 \
        -height 0 -relheight 0.058 -anchor nw -bordermode ignore 
    place $top.mes57 \
        -in $top -x 0 -relx 0.07 -y 0 -rely 0.807 -width 0 -relwidth 0.095 \
        -height 0 -relheight 0.043 -anchor nw -bordermode ignore 

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

