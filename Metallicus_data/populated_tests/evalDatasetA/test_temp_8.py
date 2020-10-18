from string_utils import *
import pytest

@pytest.mark.parametrize('value,op', [('me@foo.com', True), ('name.site.com', False), ('name@d.com', False), ('name@site', False), ('name@site.', False), ('me@foo.123', False), ('me@foo.c', False), ('me@foo.!!', False), ('me@foo.___', False), ('me@foo.toolongext', False), ('someone@SOMESITE.COM', False), ('me@#foo#.com', False), ('me@foo!.com', False), ('someone@[foo].com', False), ('name@em..ail.net', False), ('name@email..net', False), ('name@', False), ('#me#@foo.com', False), ('me!@foo.com', False), ('[][]@foo.com', False), ('john%@john5music.net', False), ('@foo.com', False), ('me@foo.com', True), ('name@gmail.com', True), ('name2@gmail.com', True), ('PeterParker@gmail.com', True), ('first_name.last_name@yahoo.it', True), ('foo@domamin.subdomain.com', True), ('is1email@domain.org', True), ('UPPER_CASE_EMAIL@somesite.com', True), (None, False), (False, False), (0, False), ([], False), ({
    'a': 1,
}, False), ('', False), (' ', False), ('email@here.com', True), ('weirder-email@here.and.there.com', True), ('email@[127.0.0.1]', True), ('example@valid-----hyphens.com', True), ('example@valid-with-hyphens.com', True), ('test@domain.with.idn.tld.\\xe0\\xa4\\x89\\xe0\\xa4\\xa6\\xe0\\xa4\\xbe\\xe0\\xa4\\xb9\\xe0\\xa4\\xb0\\xe0\\xa4\\xa3.\\xe0\\xa4\\xaa\\xe0\\xa4\\xb0\\xe0\\xa5\\x80\\xe0\\xa4\\x95\\xe0\\xa5\\x8d\\xe0\\xa4\\xb7\\xe0\\xa4\\xbe', True), ('email@localhost', True), ('email@localdomain', True), ('"test@test"@example.com', True), ('"\\\t"@here.com', True), (None, False), ('', False), ('abc', False), ('abc@', False), ('abc@bar', False), ('a @x.cz', False), ('abc@.com', False), ('something@@somewhere.com', False), ('email@127.0.0.1', False), ('example@invalid-.com', False), ('example@-invalid.com', False), ('example@inv-.alid-.com', False), ('example@inv-.-alid.com', False), ('"\\\n"@here.com', False), ('jsmith@apache.org', True), ('joe!/blow@apache.org', True), ('joe@ap/ache.org', False), ('joe@apac!he.org', False), ('andy.noble@?data-workshop.com', False), ("andy.o'reilly@data-workshop.com", True), ("andy@o'reilly.data-workshop.com", False), ('foo+bar@i.am.not.in.us.example.com', True), ('foo+bar@example+3.com', False), ('test@%*.com', False), ('test@^&#.com', False), ('joeblow @apache.org', False), ('joeblow@ apache.org', False), (' joeblow@apache.org', True), ('joeblow@apache.org ', True), ('joe blow@apache.org ', False), ('joeblow@apa che.org ', False), ('joeblow@apa,che.org', False), ('joeblow@apache.o,rg', False), ('joeblow@apache,org', False), ('andy.noble@data-workshop.com', True), ('andy-noble@data-workshop.-com', False), ('andy-noble@data-workshop.c-om', False), ('andy-noble@data-workshop.co-m', False), ('me@at&t.net', False), ('me@att.net', True), ('abc@school.school', True), ('joe@localhost.localdomain', True), ('joe@localhost', True), ('joe@localhost.localdomain', False), ('joe@localhost', False), ('Loremipsumdolorsitametconsecteturadipiscingelit.Nullavitaeligulamattisrhoncusnuncegestasmattisleo.Donecnonsapieninmagnatristiquedictumaacturpis.Fusceorciduifacilisisutsapieneuconsequatpharetralectus.Quisqueenimestpulvinarutquamvitaeportamattisex.Nullamquismaurisplaceratconvallisjustoquisportamauris.Innullalacusconvalliseufringillautvenenatissitametdiam.Maecenasluctusligulascelerisquepulvinarfeugiat.Sedmolestienullaaliquetorciluctusidpharetranislfinibus.Suspendissemalesuadatinciduntduisitametportaarcusollicitudinnec.Donecetmassamagna.Curabitururnadiampretiumveldignissimporttitorfringillaeuneque.Duisantetelluspharetraidtinciduntinterdummolestiesitametfelis.Utquisquamsitametantesagittisdapibusacnonodio.Namrutrummolestiediamidmattis.Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus.Morbiposueresedmetusacconsectetur.Etiamquisipsumvitaejustotempusmaximus.Sedultriciesplaceratvolutpat.Integerlacuslectusmaximusacornarequissagittissitametjusto.Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus.Maecenasindictumpurussedrutrumex.Nullafacilisi.Integerfinibusfinibusmietpharetranislfaucibusvel.Maecenasegetdolorlacinialobortisjustovelullamcorpersem.Vivamusaliquetpurusidvariusornaresapienrisusrutrumnisitinciduntmollissemnequeidmetus.Etiamquiseleifendpurus.Nuncfelisnuncscelerisqueiddignissimnecfinibusalibero.Nuncsemperenimnequesitamethendreritpurusfacilisisac.Maurisdapibussemperfelisdignissimgravida.Aeneanultricesblanditnequealiquamfinibusodioscelerisqueac.Aliquamnecmassaeumaurisfaucibusfringilla.Etiamconsequatligulanisisitametaliquamnibhtemporquis.Nuncinterdumdignissimnullaatsodalesarcusagittiseu.Proinpharetrametusneclacuspulvinarsedvolutpatliberoornare.Sedligulanislpulvinarnonlectuseublanditfacilisisante.Sedmollisnislalacusauctorsuscipit.Inhachabitasseplateadictumst.Phasellussitametvelittemporvenenatisfeliseuegestasrisus.Aliquameteratsitametnibhcommodofinibus.Morbiefficiturodiovelpulvinariaculis.Aeneantemporipsummassaaconsecteturturpisfaucibusultrices.Praesentsodalesmaurisquisportafermentum.Etiamnisinislvenenatisvelauctorutullamcorperinjusto.Proinvelligulaerat.Phasellusvestibulumgravidamassanonfeugiat.Maecenaspharetraeuismodmetusegetefficitur.Suspendisseamet@gmail.com', False), ('someone@xn--d1abbgf6aiiy.xn--p1ai', True), ('someone@пÑ\x80езиденÑ\x82.Ñ\x80Ñ\x84', True), ('someone@www.bücher.ch', True), ('someone@www.?.ch', False), ('someone@www.bücher.ch', True), ('someone@www.?.ch', False), ('someone@[216.109.118.76]', True), ('someone@yahoo.com', True), ('andy.noble@data-workshop.com.', False), ('someone@-test.com', False), ('someone@test-.com', False), ('joe1blow@apache.org', True), ('joe$blow@apache.org', True), ('joe-@apache.org', True), ('joe_@apache.org', True), ('joe+@apache.org', True), ('joe!@apache.org', True), ('joe*@apache.org', True), ("joe'@apache.org", True), ('joe%45@apache.org', True), ('joe?@apache.org', True), ('joe&@apache.org', True), ('joe=@apache.org', True), ('+joe@apache.org', True), ('!joe@apache.org', True), ('*joe@apache.org', True), ("'joe@apache.org", True), ('%joe45@apache.org', True), ('?joe@apache.org', True), ('&joe@apache.org', True), ('=joe@apache.org', True), ('+@apache.org', True), ('!@apache.org', True), ('*@apache.org', True), ("'@apache.org", True), ('%@apache.org', True), ('?@apache.org', True), ('&@apache.org', True), ('=@apache.org', True), ('joe.@apache.org', False), ('.joe@apache.org', False), ('.@apache.org', False), ('joe.ok@apache.org', True), ('joe..ok@apache.org', False), ('..@apache.org', False), ('joe(@apache.org', False), ('joe)@apache.org', False), ('joe,@apache.org', False), ('joe;@apache.org', False), ('"joe."@apache.org', True), ('".joe"@apache.org', True), ('"joe+"@apache.org', True), ('"joe!"@apache.org', True), ('"joe*"@apache.org', True), ('"joe\'"@apache.org', True), ('"joe("@apache.org', True), ('"joe)"@apache.org', True), ('"joe,"@apache.org', True), ('"joe%45"@apache.org', True), ('"joe;"@apache.org', True), ('"joe?"@apache.org', True), ('"joe&"@apache.org', True), ('"joe="@apache.org', True), ('".."@apache.org', True), ('"john\\"doe"@apache.org', True), ('john56789.john56789.john56789.john56789.john56789.john56789.john@example.com', True), ('john56789.john56789.john56789.john56789.john56789.john56789.john5@example.com', False), ('\\>escape\\\\special\\^characters\\<@example.com', True), ('Abc\\@def@example.com', True), ('Abc@def@example.com', False), ('space\\ monkey@example.com', True), ('test@.com', False), ('abc-@abc.com', True), ('abc_@abc.com', True), ('abc-def@abc.com', True), ('abc_def@abc.com', True), ('abc@abc_def.com', False), ('jsmith@apache.org', True), ('jsmith@apache.com', True), ('jsmith@apache.net', True), ('jsmith@apache.info', True), ('jsmith@apache.', False), ('jsmith@apache.c', False), ('someone@yahoo.museum', True), ('someone@yahoo.mu-seum', False), ('test@com', True), ('abigail@example.com', True), ('abigail@example.com ', True), (' abigail@example.com', True), ('abigail @example.com ', True), ('*@example.net', True), ('"\\""@foo.bar', True), ('fred&barny@example.com', True), ('---@example.com', True), ('foo-bar@example.net', True), ('"127.0.0.1"@[127.0.0.1]', True), ('Abigail <abigail@example.com>', True), ('Abigail<abigail@example.com>', True), ('Abigail<@a,@b,@c:abigail@example.com>', True), ('"This is a phrase"<abigail@example.com>', True), ('"Abigail "<abigail@example.com>', True), ('"Joe & J. Harvey" <example @Org>', True), ('Abigail <abigail @ example.com>', True), ('Abigail made this <  abigail   @   example  .    com    >', True), ('Abigail(the bitch)@example.com', True), ('Abigail <abigail @ example . (bar) com >', True), ('Abigail < (one)  abigail (two) @(three)example . (bar) com (quz) >', True), ('Abigail (foo) (((baz)(nested) (comment)) ! ) < (one)  abigail (two) @(three)example . (bar) com (quz) >', True), ('Abigail <abigail(fo\\(o)@example.com>', True), ('Abigail <abigail(fo\\)o)@example.com> ', True), ('(foo) abigail@example.com', True), ('abigail@example.com (foo)', True), ('"Abi\\"gail" <abigail@example.com>', True), ('abigail@[example.com]', True), ('abigail@[exa\\[ple.com]', True), ('abigail@[exa\\]ple.com]', True), ('":sysmail"@  Some-Group. Some-Org', True), ('Muhammed.(I am  the greatest) Ali @(the)Vegas.WBA', True), ('mailbox.sub1.sub2@this-domain', True), ('sub-net.mailbox@sub-domain.domain', True), ('name:;', True), ("':;", True), ('name:   ;', True), ('Alfred Neuman <Neuman@BBN-TENEXA>', True), ('Neuman@BBN-TENEXA', True), ('"George, Ted" <Shared@Group.Arpanet>', True), ('Wilt . (the  Stilt) Chamberlain@NBA.US', True), ('Cruisers:  Port@Portugal, Jones@SEA;', True), ('$@[]', True), ('*()@[]', True), ('"quoted ( brackets" ( a comment )@example.com', True), ('"Joe & J. Harvey"\\x0D\\x0A     <ddd\\@ Org>', True), ('"Joe &\\x0D\\x0A J. Harvey" <ddd \\@ Org>', True), ('Gourmets:  Pompous Person <WhoZiWhatZit\\@Cordon-Bleu>,\\x0D\\x0A        Childs\\@WGBH.Boston, "Galloping Gourmet"\\@\\x0D\\x0A        ANT.Down-Under (Australian National Television),\\x0D\\x0A        Cheapie\\@Discount-Liquors;', True), ('   Just a string', False), ('string', False), ('(comment)', False), ('()@example.com', False), ('fred(&)barny@example.com', False), ('fred\\ barny@example.com', False), ('Abigail <abi gail @ example.com>', False), ('Abigail <abigail(fo(o)@example.com>', False), ('Abigail <abigail(fo)o)@example.com>', False), ('"Abi"gail" <abigail@example.com>', False), ('abigail@[exa]ple.com]', False), ('abigail@[exa[ple.com]', False), ('abigail@[exaple].com]', False), ('abigail@', False), ('@example.com', False), ('phrase: abigail@example.com abigail@example.com ;', False), ('invalid�char@example.com', False), ('jsmith@apache.org', True), ('joe!/blow@apache.org', True), ('joe@ap/ache.org', False), ('joe@apac!he.org', False), ('andy.noble@?data-workshop.com', False), ("andy.o'reilly@data-workshop.com", True), ("andy@o'reilly.data-workshop.com", False), ('foo+bar@i.am.not.in.us.example.com', True), ('foo+bar@example+3.com', False), ('test@%*.com', False), ('test@^&#.com', False), ('joeblow @apache.org', False), ('joeblow@ apache.org', False), (' joeblow@apache.org', True), ('joeblow@apache.org ', True), ('joe blow@apache.org ', False), ('joeblow@apa che.org ', False), ('joeblow@apa,che.org', False), ('joeblow@apache.o,rg', False), ('joeblow@apache,org', False), ('andy.noble@data-workshop.com', True), ('andy-noble@data-workshop.-com', False), ('andy-noble@data-workshop.c-om', False), ('andy-noble@data-workshop.co-m', False), ('me@at&t.net', False), ('me@att.net', True), ('abc@school.school', True), ('joe@localhost.localdomain', True), ('joe@localhost', True), ('joe@localhost.localdomain', False), ('joe@localhost', False), ('Loremipsumdolorsitametconsecteturadipiscingelit.Nullavitaeligulamattisrhoncusnuncegestasmattisleo.Donecnonsapieninmagnatristiquedictumaacturpis.Fusceorciduifacilisisutsapieneuconsequatpharetralectus.Quisqueenimestpulvinarutquamvitaeportamattisex.Nullamquismaurisplaceratconvallisjustoquisportamauris.Innullalacusconvalliseufringillautvenenatissitametdiam.Maecenasluctusligulascelerisquepulvinarfeugiat.Sedmolestienullaaliquetorciluctusidpharetranislfinibus.Suspendissemalesuadatinciduntduisitametportaarcusollicitudinnec.Donecetmassamagna.Curabitururnadiampretiumveldignissimporttitorfringillaeuneque.Duisantetelluspharetraidtinciduntinterdummolestiesitametfelis.Utquisquamsitametantesagittisdapibusacnonodio.Namrutrummolestiediamidmattis.Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus.Morbiposueresedmetusacconsectetur.Etiamquisipsumvitaejustotempusmaximus.Sedultriciesplaceratvolutpat.Integerlacuslectusmaximusacornarequissagittissitametjusto.Cumsociisnatoquepenatibusetmagnisdisparturientmontesnasceturridiculusmus.Maecenasindictumpurussedrutrumex.Nullafacilisi.Integerfinibusfinibusmietpharetranislfaucibusvel.Maecenasegetdolorlacinialobortisjustovelullamcorpersem.Vivamusaliquetpurusidvariusornaresapienrisusrutrumnisitinciduntmollissemnequeidmetus.Etiamquiseleifendpurus.Nuncfelisnuncscelerisqueiddignissimnecfinibusalibero.Nuncsemperenimnequesitamethendreritpurusfacilisisac.Maurisdapibussemperfelisdignissimgravida.Aeneanultricesblanditnequealiquamfinibusodioscelerisqueac.Aliquamnecmassaeumaurisfaucibusfringilla.Etiamconsequatligulanisisitametaliquamnibhtemporquis.Nuncinterdumdignissimnullaatsodalesarcusagittiseu.Proinpharetrametusneclacuspulvinarsedvolutpatliberoornare.Sedligulanislpulvinarnonlectuseublanditfacilisisante.Sedmollisnislalacusauctorsuscipit.Inhachabitasseplateadictumst.Phasellussitametvelittemporvenenatisfeliseuegestasrisus.Aliquameteratsitametnibhcommodofinibus.Morbiefficiturodiovelpulvinariaculis.Aeneantemporipsummassaaconsecteturturpisfaucibusultrices.Praesentsodalesmaurisquisportafermentum.Etiamnisinislvenenatisvelauctorutullamcorperinjusto.Proinvelligulaerat.Phasellusvestibulumgravidamassanonfeugiat.Maecenaspharetraeuismodmetusegetefficitur.Suspendisseamet@gmail.com', False), ('someone@xn--d1abbgf6aiiy.xn--p1ai', True), ('someone@пÑ\x80езиденÑ\x82.Ñ\x80Ñ\x84', True), ('someone@www.bücher.ch', True), ('someone@www.?.ch', False), ('someone@www.bücher.ch', True), ('someone@www.?.ch', False), ('someone@[216.109.118.76]', True), ('someone@yahoo.com', True), ('andy.noble@data-workshop.com.', False), ('someone@-test.com', False), ('someone@test-.com', False), ('joe1blow@apache.org', True), ('joe$blow@apache.org', True), ('joe-@apache.org', True), ('joe_@apache.org', True), ('joe+@apache.org', True), ('joe!@apache.org', True), ('joe*@apache.org', True), ("joe'@apache.org", True), ('joe%45@apache.org', True), ('joe?@apache.org', True), ('joe&@apache.org', True), ('joe=@apache.org', True), ('+joe@apache.org', True), ('!joe@apache.org', True), ('*joe@apache.org', True), ("'joe@apache.org", True), ('%joe45@apache.org', True), ('?joe@apache.org', True), ('&joe@apache.org', True), ('=joe@apache.org', True), ('+@apache.org', True), ('!@apache.org', True), ('*@apache.org', True), ("'@apache.org", True), ('%@apache.org', True), ('?@apache.org', True), ('&@apache.org', True), ('=@apache.org', True), ('joe.@apache.org', False), ('.joe@apache.org', False), ('.@apache.org', False), ('joe.ok@apache.org', True), ('joe..ok@apache.org', False), ('..@apache.org', False), ('joe(@apache.org', False), ('joe)@apache.org', False), ('joe,@apache.org', False), ('joe;@apache.org', False), ('"joe."@apache.org', True), ('".joe"@apache.org', True), ('"joe+"@apache.org', True), ('"joe!"@apache.org', True), ('"joe*"@apache.org', True), ('"joe\'"@apache.org', True), ('"joe("@apache.org', True), ('"joe)"@apache.org', True), ('"joe,"@apache.org', True), ('"joe%45"@apache.org', True), ('"joe;"@apache.org', True), ('"joe?"@apache.org', True), ('"joe&"@apache.org', True), ('"joe="@apache.org', True), ('".."@apache.org', True), ('"john\\"doe"@apache.org', True), ('john56789.john56789.john56789.john56789.john56789.john56789.john@example.com', True), ('john56789.john56789.john56789.john56789.john56789.john56789.john5@example.com', False), ('\\>escape\\\\special\\^characters\\<@example.com', True), ('Abc\\@def@example.com', True), ('Abc@def@example.com', False), ('space\\ monkey@example.com', True), ('test@.com', False), ('abc-@abc.com', True), ('abc_@abc.com', True), ('abc-def@abc.com', True), ('abc_def@abc.com', True), ('abc@abc_def.com', False), ('jsmith@apache.org', True), ('jsmith@apache.com', True), ('jsmith@apache.net', True), ('jsmith@apache.info', True), ('jsmith@apache.', False), ('jsmith@apache.c', False), ('someone@yahoo.museum', True), ('someone@yahoo.mu-seum', False), ('test@com', True), ('abigail@example.com', True), ('abigail@example.com ', True), (' abigail@example.com', True), ('abigail @example.com ', True), ('*@example.net', True), ('"\\""@foo.bar', True), ('fred&barny@example.com', True), ('---@example.com', True), ('foo-bar@example.net', True), ('"127.0.0.1"@[127.0.0.1]', True), ('Abigail <abigail@example.com>', True), ('Abigail<abigail@example.com>', True), ('Abigail<@a,@b,@c:abigail@example.com>', True), ('"This is a phrase"<abigail@example.com>', True), ('"Abigail "<abigail@example.com>', True), ('"Joe & J. Harvey" <example @Org>', True), ('Abigail <abigail @ example.com>', True), ('Abigail made this <  abigail   @   example  .    com    >', True), ('Abigail(the bitch)@example.com', True), ('Abigail <abigail @ example . (bar) com >', True), ('Abigail < (one)  abigail (two) @(three)example . (bar) com (quz) >', True), ('Abigail (foo) (((baz)(nested) (comment)) ! ) < (one)  abigail (two) @(three)example . (bar) com (quz) >', True), ('Abigail <abigail(fo\\(o)@example.com>', True), ('Abigail <abigail(fo\\)o)@example.com> ', True), ('(foo) abigail@example.com', True), ('abigail@example.com (foo)', True), ('"Abi\\"gail" <abigail@example.com>', True), ('abigail@[example.com]', True), ('abigail@[exa\\[ple.com]', True), ('abigail@[exa\\]ple.com]', True), ('":sysmail"@  Some-Group. Some-Org', True), ('Muhammed.(I am  the greatest) Ali @(the)Vegas.WBA', True), ('mailbox.sub1.sub2@this-domain', True), ('sub-net.mailbox@sub-domain.domain', True), ('name:;', True), ("':;", True), ('name:   ;', True), ('Alfred Neuman <Neuman@BBN-TENEXA>', True), ('Neuman@BBN-TENEXA', True), ('"George, Ted" <Shared@Group.Arpanet>', True), ('Wilt . (the  Stilt) Chamberlain@NBA.US', True), ('Cruisers:  Port@Portugal, Jones@SEA;', True), ('$@[]', True), ('*()@[]', True), ('"quoted ( brackets" ( a comment )@example.com', True), ('"Joe & J. Harvey"\\x0D\\x0A     <ddd\\@ Org>', True), ('"Joe &\\x0D\\x0A J. Harvey" <ddd \\@ Org>', True), ('Gourmets:  Pompous Person <WhoZiWhatZit\\@Cordon-Bleu>,\\x0D\\x0A        Childs\\@WGBH.Boston, "Galloping Gourmet"\\@\\x0D\\x0A        ANT.Down-Under (Australian National Television),\\x0D\\x0A        Cheapie\\@Discount-Liquors;', True), ('   Just a string', False), ('string', False), ('(comment)', False), ('()@example.com', False), ('fred(&)barny@example.com', False), ('fred\\ barny@example.com', False), ('Abigail <abi gail @ example.com>', False), ('Abigail <abigail(fo(o)@example.com>', False), ('Abigail <abigail(fo)o)@example.com>', False), ('"Abi"gail" <abigail@example.com>', False), ('abigail@[exa]ple.com]', False), ('abigail@[exa[ple.com]', False), ('abigail@[exaple].com]', False), ('abigail@', False), ('@example.com', False), ('phrase: abigail@example.com abigail@example.com ;', False), ('invalid�char@example.com', False)])
def test_email(value, op):
    assert (is_email(value) == op)