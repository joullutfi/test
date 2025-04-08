using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Collections.Specialized.BitVector32;
using System.Xml.Linq;

< odoo >
    < template id = "snippet" name = "Snippet" >
        < section class= "index_snippet" >
            < div class= "snippet" >
                < h1 >
                    Attractive Page
                </ h1 >
            </ div >
        </ section >
    </ template >

    < template id = "index_banner" inherit_id = "website.snippets"
        name = "Index Banner" >
        < xpath expr = "//div[@id='snippet_structure']/div[@class='o_panel_body']"
            position = "inside" >
            < t - snippet = "website.snippet.snippet" />
        </ xpath >
    </ template >
</ odoo >
kjj