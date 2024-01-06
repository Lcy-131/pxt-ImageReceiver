radio.onReceivedValue(function (display_command_name, display_command_value) {
    if (display_command_name.substr(0, 1) == "xy") {
        ix2 = parseFloat(display_command_name.charAt(0))
        iy2 = parseFloat(display_command_name.charAt(1))
        if (display_command_value != 0) {
            if (led.pointBrightness(ix2, iy2) != display_command_value) {
                led.plotBrightness(ix2, iy2, display_command_value)
            }
        } else if (led.point(ix2, iy2)) {
            led.unplot(ix2, iy2)
        }
    } else if (display_command_name == "num") {
        basic.showNumber(display_command_value)
    }
})
radio.onReceivedNumber(function (game_score) {
    if (game_score == -1) {
        display_killer = 0
    } else {
        score = game_score
        display_killer = 1
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
let score = 0
let display_killer = 0
let iy2 = 0
let ix2 = 0
radio.setGroup(1)
