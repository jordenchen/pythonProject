(function() {
    var ModAddress = Process.findModuleByName('WeChatWin.dll');
    var hookAddress = ModAddress.base.add('0x5FE9C0');
    Interceptor.attach(hookAddress, {
        onEnter: function (args) {
            var xml_li = [];
            var edi = this.context.edi;
            var edi1 = Memory.readInt(edi);
            var edi2 = Memory.readInt(edi.add('0x4'));
            var num = (edi2 - edi1) /672 ;
            for(var i=1; i<num+1; i++){
                var xml = Memory.readUtf16String(Memory.readPointer(Memory.readPointer(edi).add('0x70'*i)));
                console.log('xml-song');
                xml_li.push(xml);
            }
            send({'xml': xml_li});
        }
    });
})();