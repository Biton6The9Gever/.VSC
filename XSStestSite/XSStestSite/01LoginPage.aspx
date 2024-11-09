<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="01LoginPage.aspx.cs" Inherits="XSStestSite._01LoginPage" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>plews no hakc me</title>
</head>
<body>
    <form id="form1" runat="server">
        <div style="text-align:center;">
            <asp:TextBox ID="txtUsername" runat="server" placeholder="Username"></asp:TextBox><br />
            <asp:TextBox ID="txtPassword" runat="server" placeholder="Password"></asp:TextBox><br />
            <asp:Button ID="btnSubmit" Text="Submit" runat="server" OnClick="btnSubmit_Click"/>
        </div>
    </form>
</body>
</html>
