import unittest
import ParseData.Filter as Filter


class FilterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data: str = """<table align="center" border="1" bordercolor="#EAEAEA" cellpadding="1" cellspacing="0" width="100%">
<tbody><tr>
<td bgcolor="#0000CE" height="25" nowrap="" width="0">
<span class="style26"><font face="Arial, Helvetica, sans-serif">
      
 Sem 
 
      </font></span></td>
<td bgcolor="#0000CE"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Class Code
      
    </font></span></td>
<td bgcolor="#0000CE"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Learning Module
      
    </font></span></td>
<td bgcolor="#0000CE"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Instructor
      
    </font></span></td>
<td bgcolor="#0000CE" width="0"><span class="style26"><font face="Arial, Helvetica, sans-serif">
      
      Venue
      
    </font></span></td>
<td bgcolor="#0000CE" width="0"><div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
      Period
      
    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="0"><div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
      Time
      
    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style35"><font face="Arial, Helvetica, sans-serif">
      
Sun

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Mon

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Tue

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Wed

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34"><strong><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Thu

    </font></span></strong></div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style34 style36">
<div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">
        
  Fri
  
      </font></div>
</div></td>
<td bgcolor="#0000CE" width="16"> <div align="center" class="style37"><span class="style5"><font face="Arial, Helvetica, sans-serif">
      
Sat

    </font></span></div></td>
</tr>
<tr>
<td bgcolor="#FFFFE6"><div align="center" class="style5"><font face="Arial, Helvetica, sans-serif">       2    </font></div></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       COMP221-221    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       OBJECT ORIENTED TECHNOLOGIES    </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       WONG UN HONG     </font></span></td>
<td bgcolor="#FFFFE6"><span class="style5"><font face="Arial, Helvetica, sans-serif">       N_54 </font></span></td>
<td bgcolor="#FFFFE6" width="200"><span class="style5"><font face="Arial, Helvetica, sans-serif">
		2023/01/05-2023/04/22

		</font></span></td>
<td bgcolor="#FFFFE6" nowrap=""><span class="style5"><font face="Arial, Helvetica, sans-serif">       10:00-11:30     </font></span></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    

    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif">
<img align="absmiddle" height="16" src="images/dot.gif" width="16"/>
</font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
<td align="center" bgcolor="#FFFFE6"> <div align="center"><font size="1"><b><font face="Arial, Helvetica, sans-serif"> 
	  	
		   
		    
    </font></b></font></div></td>
</tr>
</tbody>
</table>"""

    def tearDown(self) -> None:
        self.data = None

    def test_NBSPFilter(self) -> None:
        nbsp_filter: Filter.NBSPFilter = Filter.NBSPFilter(self.data)
        self.assertEqual(nbsp_filter.get_data(), self.data.replace(" ", " "))
