(function(){
    var ModAddress = Process.findModuleByName('WeChatWin.dll');
    var hookAddress = ModAddress.base.add('0x5FE9C0');
    Interceptor.attach(hookAddress, {
        onEnter: function (args) {
            console.log('hook-start');
            var xml_li = [];
            var edi = this.context.edi;
            var edi1 = Memory.readInt(edi);
            var edi2 = Memory.readInt(edi.add('0x4'));
            var num = (edi2 - edi1) /672 ;
            for(var i=0; i<num; i++){
                var leiji = (112 + 672*i);
                var pointer_jia = '0x' + leiji.toString(16);
                console.log(pointer_jia);
                var xml = Memory.readUtf16String(Memory.readPointer(Memory.readPointer(edi).add(pointer_jia)));
                xml_li.push(xml);
             }
            console.log('xml_li_fasong');
            send({'xml_li': xml_li});
        }
    });
})();