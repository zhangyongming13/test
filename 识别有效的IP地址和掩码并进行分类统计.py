def cheackmask(MaskList):
    zhang = []
    for i in MaskList:
        zhang.append(str(bin(int(i)))[2:])
    zhang = ''.join(zhang)
    MaskFlag = 0
    if '0' not in zhang or '1' not in zhang:
        return False
    for i in zhang:
        if i == '0':
            MaskFlag += 1
        if i == '1' and MaskFlag != 0:
            return False
    return True


def cheackip(IpList):
    # 判断IP地址格式是否正确
    if len(IpList) != 4:
        return False
    if '' in IpList:
        return False
    if int(IpList[0]) <= 0:
        return False
    else:
        for i in IpList:
            if int(i) < 0 or int(i) > 255:
                return False
    return True


if __name__ == '__main__':
    ip_mask_list = []
    while True:
        try:
            ip_mask = str(input()).strip()
            if ip_mask == '':
                break
            ip_mask_list.append(ip_mask)
        except:
            break
    A_IP = 0
    B_IP = 0
    C_IP = 0
    D_IP = 0
    E_IP = 0
    Wrong_IP_OR_MASK = 0
    PrivateIP = 0

    for ip_mask in ip_mask_list:
        ip = ip_mask.split('~')[0].strip()
        mask = ip_mask.split('~')[-1].strip()

        mask_list = mask.split('.')
        IpList = ip.split('.')
        # 判断IP地址的类别，如果IP地址格式错误就不需要判断了
        if cheackip(IpList) and cheackmask(mask_list):
            # 判断ABCDE类
            if 1 <= int(IpList[0]) <= 126:
                A_IP += 1
            elif 128 <= int(IpList[0]) <= 191:
                B_IP += 1
            elif 192 <= int(IpList[0]) <= 223:
                C_IP += 1
            elif 224 <= int(IpList[0]) <= 239:
                D_IP += 1
            elif 240 <= int(IpList[0]) <= 255:
                E_IP += 1
            if int(IpList[0]) == 10:
                PrivateIP += 1
            if int(IpList[0]) == 172:
                if 16 <= int(IpList[1]) <= 31:
                    PrivateIP += 1
                else:
                    B_IP += 1
            if int(IpList[0]) == 192 and int(IpList[1]) == 168:
                PrivateIP += 1
        else:
            Wrong_IP_OR_MASK += 1
    print('%d %d %d %d %d %d %d' %(A_IP, B_IP, C_IP, D_IP, E_IP, Wrong_IP_OR_MASK, PrivateIP))
