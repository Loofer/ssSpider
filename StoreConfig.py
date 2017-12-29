text = 'this is may\n text'


def updateStr(tables):
    str=''
    prifix ="{ 	\n" \
            "\"configs\" : [\n"
    for i in range(len(tables)):
        server = tables[i].get("ip")
        port = tables[i].get("port")
        password = tables[i].get("password")
        method = tables[i].get("method")
        id = tables[i].get("id")
        str3 = "   {        \n" \
             "            \"remarks\":\"\",\n" \
             "            \"id\":\""+id+"\",\n" \
             "            \"server\":\""+server+"\",\n" \
             "            \"server_port\":\""+port+"\",\n" \
             "            \"server_udp_port\":0,\n" \
             "            \"password\":\""+password+"\",\n" \
             "            \"method\":\""+method+"\",\n" \
             "            \"protocol\":\"origin\",\n" \
             "            \"protocolparam\":\"\",\n" \
             "            \"obfs\":\"plain\",\n" \
             "            \"obfsparam\":\"\",\n" \
             "            \"remarks_base64\":\"\",\n" \
             "            \"group\":\"\",\n" \
             "            \"enable\":true,\n" \
             "            \"udp_over_tcp\":false,\n" \
                                                "    }"
        if i != len(tables) - 1:
            str += str3 + ",\n"
        else:
            str += str3

    # print(str3+",\n"+str3)

    input = open('template.text')
    endFix = input.read()
    text = prifix + str + endFix
    file_object = open('gui-config.json', 'w')

    file_object.write(text)
    input.close()
    file_object.close()

