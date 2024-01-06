radio.onReceivedValue(function (display_command_name, display_command_value) {
    if (display_command_name.charAt(0) == "x" && display_command_name.charAt(2) == "y") {
        ix = parseFloat(display_command_name.charAt(0))
        iy = parseFloat(display_command_name.charAt(2))
        if (display_command_value != 0) {
            if (led.pointBrightness(ix, iy) != display_command_value) {
                led.plotBrightness(ix, iy, display_command_value)
            }
        } else if (led.point(ix, iy)) {
            led.unplot(ix, iy)
        }
    } else if (display_command_name == "num") {
        basic.showNumber(display_command_value)
    }
})
radio.onReceivedString(function (display_photo) {
    display_list = []
    list_tmp = ""
    for (let display_index of display_photo) {
        if (display_index == "`") {
            display_list.push(parseFloat(list_tmp))
            list_tmp = ""
            continue;
        }
        list_tmp = "" + list_tmp + display_index
    }
    for (let ix = 0; ix <= 4; ix++) {
        for (let iy = 0; iy <= 4; iy++) {
            led.unplot(ix, iy)
            led.plotBrightness(ix, iy, display_list[ix * 5 + iy])
        }
    }
})
let list_tmp = ""
let display_list: number[] = []
let iy = 0
let ix = 0
radio.setGroup(1)
