(function() {
    var ModAddress = Process.findModuleByName('WeChatWin.dll');
    var hookAddress = ModAddress.base.add('0x5A6D20');
    Interceptor.attach(hookAddress, {
        onEnter: function (args) {
            var edi = this.context.edi;
            var emu = Memory.readPointer(edi);
            var xml = Memory.readUtf16String(Memory.readPointer(emu.add('0x70')));
            send({'xml': xml});

        }
    });
})();