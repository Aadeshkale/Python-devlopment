s={(12,'lokesh','comp',22),
(13,'rachna','elec',19),
(14,'Aadesh','entc',24),
(18,'Kunal','mech',21),
(15,'Mahesh','comp',19),
(15,'Mahesh','comp',19),
(15,'Mahesh','comp',19),
(15,'Mahesh','comp',19),
(16,'Raj','civil',40),
(17,'sucita','comp',20),
(17,'sucita','comp',20),
(17,'sucita','comp',20),
}
# unpacking
for id ,name ,*_  in s:
    print(id,"->",name)
