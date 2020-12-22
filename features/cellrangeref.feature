Feature: Define a dimension as a range of values from a cell reference.
  I want to be able to define a dimension as a range of values from a cell reference.

  Scenario: Define year from a range of cell references.
    Given we load an xls file named "bulletindataset2v2.xlsx"
    And get "some_name" from the transform:
    """
    def transform_xlsx():
        tabs = [x for x in tabs if x.name.strip() == "Table 2a"]
        return tabs
    """
    And we define year as the values in cells "A11:A250"
    Then we confirm year is defined as type cell, equal to:
    """
    <class 'xypath.xypath.Bag'>
    """

Scenario: Define year as correct cells.
    Given we load an xls file named "bulletindataset2v2.xlsx"
    And get "some_name" from the transform:
    """
    def transform_xlsx()):
        tabs = [x for x in tabs if x.name.strip() == "Table 2a"]
        return tabs
    """
    And we define year as the values in cells "A11:A250" 
    Then we confirm that year is equal to:
    """
    {<A104 ''>, <A62 ''>, <A55 2002.0>, <A97 ''>, <A170 ''>, <A179 ''>, <A102 ''>, <A60 ''>, <A120 ''>, <A177 ''>, <A100 ''>, <A58 ''>, <A77 ''>, <A118 ''>, <A191 ''>, <A136 ''>, <A226 2018.0>, <A116 ''>, <A93 ''>, <A134 ''>, <A82 ''>, <A110 ''>, <A132 ''>, <A24 2010.0>, <A96 ''>, <A57 ''>, <A108 ''>, <A34 ''>, <A27 2013.0>, <A106 ''>, <A48 ''>, <A37 ''>, <A113 ''>, <A194 ''>, <A53 ''>, <A72 ''>, <A43 1999.0>, <A142 2011.0>, <A75 2007.0>, <A208 ''>, <A70 ''>, <A169 ''>, <A111 2016.0>, <A107 2015.0>, <A119 2018.0>, <A68 ''>, <A215 ''>, <A17 2003.0>, <A45 ''>, <A227 ''>, <A213 ''>, <A232 ''>, <A225 ''>, <A103 2014.0>, <A230 ''>, <A188 ''>, <A239 ''>, <A50 ''>, <A248 ''>, <A228 ''>, <A186 ''>, <A205 ''>, <A64 ''>, <A131 ''>, <A246 ''>, <A12 1998.0>, <A203 ''>, <A11 1997.0>, <A129 ''>, <A244 ''>, <A221 ''>, <A105 ''>, <A143 ''>, <A210 ''>, <A152 ''>, <A219 ''>, <A224 ''>, <A150 ''>, <A185 ''>, <A236 ''>, <A162 ''>, <A15 2001.0>, <A126 ''>, <A148 ''>, <A167 ''>, <A234 ''>, <A176 ''>, <A243 ''>, <A137 ''>, <A124 ''>, <A115 2017.0>, <A165 ''>, <A67 2005.0>, <A241 ''>, <A183 ''>, <A32 2018.0>, <A33 2019.0>, <A122 ''>, <A127 2020.0>, <A140 ''>, <A181 ''>, <A200 ''>, <A238 2019.0>, <A22 2008.0>, <A65 ''>, <A158 ''>, <A138 ''>, <A147 ''>, <A198 ''>, <A250 2020.0>, <A156 ''>, <A88 ''>, <A145 ''>, <A196 ''>, <A214 2017.0>, <A173 ''>, <A86 ''>, <A121 ''>, <A159 ''>, <A98 ''>, <A13 1999.0>, <A171 ''>, <A84 ''>, <A61 ''>, <A112 ''>, <A73 ''>, <A20 2006.0>, <A101 ''>, <A78 ''>, <A25 2011.0>, <A83 2009.0>, <A192 ''>, <A153 ''>, <A76 ''>, <A47 2000.0>, <A117 ''>, <A94 ''>, <A190 2015.0>, <A135 ''>, <A74 ''>, <A99 2013.0>, <A233 ''>, <A92 ''>, <A133 ''>, <A95 2012.0>, <A81 ''>, <A16 2002.0>, <A90 ''>, <A109 ''>, <A178 2014.0>, <A40 ''>, <A18 2004.0>, <A202 2016.0>, <A38 ''>, <A114 ''>, <A56 ''>, <A36 ''>, <A123 2019.0>, <A128 ''>, <A195 ''>, <A54 ''>, <A89 ''>, <A28 2014.0>, <A26 2012.0>, <A193 ''>, <A52 ''>, <A59 2003.0>, <A130 2010.0>, <A207 ''>, <A69 ''>, <A216 ''>, <A46 ''>, <A249 ''>, <A44 ''>, <A30 2016.0>, <A212 ''>, <A231 ''>, <A42 ''>, <A189 ''>, <A240 ''>, <A201 ''>, <A71 2006.0>, <A229 ''>, <A187 ''>, <A206 ''>, <A49 ''>, <A247 ''>, <A35 1997.0>, <A87 2010.0>, <A204 ''>, <A245 ''>, <A19 2005.0>, <A222 ''>, <A144 ''>, <A63 2004.0>, <A211 ''>, <A220 ''>, <A209 ''>, <A151 ''>, <A218 ''>, <A237 ''>, <A163 ''>, <A223 ''>, <A29 2015.0>, <A149 ''>, <A168 ''>, <A235 ''>, <A23 2009.0>, <A161 ''>, <A125 ''>, <A91 2011.0>, <A175 ''>, <A242 ''>, <A184 ''>, <A164 ''>, <A141 ''>, <A166 2013.0>, <A182 ''>, <A217 ''>, <A66 ''>, <A51 2001.0>, <A139 ''>, <A14 2000.0>, <A31 2017.0>, <A154 2012.0>, <A79 2008.0>, <A180 ''>, <A157 ''>, <A80 ''>, <A199 ''>, <A41 ''>, <A21 2007.0>, <A146 ''>, <A197 ''>, <A155 ''>, <A174 ''>, <A39 1998.0>, <A160 ''>, <A172 ''>, <A85 ''>}
    """    
