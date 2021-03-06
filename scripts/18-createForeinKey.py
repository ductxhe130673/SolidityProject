import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = '123456',
    database="soliditycpn"
)
mycursor = db.cursor()
mycursor.execute("""alter table Contact ADD CONSTRAINT fk_idCA1 FOREIGN KEY(aid)
references Account (aid);""")
mycursor.execute("""alter table SmartContract ADD CONSTRAINT fk_idSCA2 FOREIGN KEY(aid)
references Account (aid);""")
mycursor.execute("""alter table History ADD CONSTRAINT fk_id3HA FOREIGN KEY(aid)
references Account (aid);""")
mycursor.execute("""alter table History_Type ADD CONSTRAINT fk_id4HTH FOREIGN KEY(hid)
references History (hid);""")
mycursor.execute("""alter table Functions ADD CONSTRAINT fk_id5FSC FOREIGN KEY(sid)
references SmartContract (sid);""")
mycursor.execute("""alter table GlobalVariable ADD CONSTRAINT fk_id6GSC FOREIGN KEY(sid)
references SmartContract (sid);""")
mycursor.execute("""alter table LocalVariable ADD CONSTRAINT fk_id7LF FOREIGN KEY(fid)
references Functions (fid);""")
mycursor.execute("""alter table Argument ADD CONSTRAINT fk_id8AF FOREIGN KEY(fid)
references Functions (fid);""")
mycursor.execute("""alter table CheckedBatchSC ADD CONSTRAINT fk_id9CBA FOREIGN KEY(aid)
references Account (aid);""")
mycursor.execute("""alter table CheckedBatchSC ADD CONSTRAINT fk_id10CBL FOREIGN KEY(lnid)
references LNAFile (lnid);""")
mycursor.execute("""alter table CheckedBatchSC ADD CONSTRAINT fk_id11CBLT FOREIGN KEY(lteid)
references LTLTemplate (lteid);""")
mycursor.execute("""alter table CheckedBatchSC ADD CONSTRAINT fk_id12CBCC FOREIGN KEY(cid)
references CPNContext (cid);""")
mycursor.execute("""alter table CheckedBatchSC ADD CONSTRAINT fk_id13CBim FOREIGN KEY(imid)
references InitialMarking (imid);""")
mycursor.execute("""alter table Balance ADD CONSTRAINT fk_id14BIM FOREIGN KEY(imid)
references InitialMarking (imid);""")
mycursor.execute("""alter table IMFunction ADD CONSTRAINT fk_id15IMFIM FOREIGN KEY(imid)
references InitialMarking (imid);""")
mycursor.execute("""alter table IMArgument ADD CONSTRAINT fk_id16BIMFA FOREIGN KEY(imfid)
references IMFunction (imid);""")
mycursor.execute("""alter table CheckedSmartContractDetail ADD CONSTRAINT fk_id17SCDSC FOREIGN KEY(sid)
references SmartContract (sid);""")
mycursor.execute("""alter table CheckedSmartContractDetail ADD CONSTRAINT fk_id18SCDCBSC FOREIGN KEY(bid)
references CheckedBatchSC (bid);""")
mycursor.execute("""alter table LTLTemplate ADD CONSTRAINT fk_id19LTL FOREIGN KEY(aid)
references Account (aid);""")
mycursor.execute("""alter table CPNContext ADD CONSTRAINT fk_id20CPN FOREIGN KEY(aid)
references Account (aid);""")
