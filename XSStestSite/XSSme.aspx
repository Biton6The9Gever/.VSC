<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="XSSme.aspx.cs" Inherits="XSStestSite.XSSme" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div style="text-align:center;">
            <asp:TextBox ID="txtInput" runat="server"></asp:TextBox> <br />
            <asp:Label ID="lblOutput" runat="server" Text="Label"></asp:Label><br />
            <asp:Button ID="btnSubmit" runat="server" Text="Submit" OnClick="btnSubmit_Click" /><br />
        </div>
    </form>
</body>
</html>
