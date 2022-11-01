(function() {
    var ModAddress = Process.findModuleByName('WeChatWin.dll');
    var hookAddress = ModAddress.base.add('0x759654');
    Interceptor.attach(hookAddress, {
        onEnter: function (args) {
            var esi = this.context.esi;
            var emu = Memory.readPointer(esi);
            var leixing = Memory.readInt(emu.add('0x4C'));
            if (leixing == 15) {
                var leixing = '公众号';
                var ebp = this.context.ebp;
                var xmlPro = Memory.readPointer(ebp.add('0x6C'));
                var xml = Memory.readUtf16String(Memory.readPointer(xmlPro.add('0x70')));
                send({'xml': xml, 'leixing': leixing});
            } else if (leixing == 20) {
                var leixing = '群消息';
                var xml = Memory.readUtf16String(Memory.readPointer(emu.add('0x70')));
                send({'xml': xml, 'leixing': leixing});
            } else if (leixing == 19) {
                var leixing = '个人消息';
                var xml = Memory.readUtf16String(Memory.readPointer(emu.add('0x70')));
                send({'xml': xml, 'leixing': leixing});
            } else {
                var xml = Memory.readUtf16String(Memory.readPointer(emu.add('0x70')));
                send({'xml': xml, 'leixing': leixing});
            }

        }
    });
})();