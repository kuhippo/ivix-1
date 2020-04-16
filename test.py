import tushare as ts



if __name__ == '__main__':
    pro = ts.pro_api('7a322a3755b728f9b032ce14f864ba2294cc0c6cd0bb43529e5e01e0')
    df = pro.opt_basic(exchange='SSE')
    for df_index in df.index:
        # 将DataFrame中的一行数据转dict
        doc = dict(df.loc[df_index])
        print(doc)
    df2 = pro.opt_daily(exchange="SSE",trade_date="20150624")

    arr = []
    for df_index in df2.index:
        # 将DataFrame中的一行数据转dict
        doc = dict(df2.loc[df_index])
        print(doc)
        arr.append(doc)

    print(len(arr))

    print(df2.index)
    #
    # print(df2)
    #
    # df3 = pro.opt_daily(exchange="SSE",)
    #
    # print(df3)
