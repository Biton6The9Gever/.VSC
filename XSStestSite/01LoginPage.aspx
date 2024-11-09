<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="01LoginPage.aspx.cs" Inherits="XSStestSite._01LoginPage" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Krusty Krab Login</title>
    <link href="10LoginStyle.css" rel="stylesheet" />
</head>

<body>
    <form id="form1" runat="server">
        <div class="login-container">
            <h1>Welcome to the Krusty Krab!</h1>
            <p>Please Don't Steal the Secret Formula!</p>

            <asp:TextBox ID="txtUsername" runat="server" CssClass="styled-input" placeholder="Username"></asp:TextBox><br />
            <asp:TextBox ID="txtPassword" runat="server" CssClass="styled-input" TextMode="Password" placeholder="Password"></asp:TextBox><br />
            <asp:Button ID="btnSubmit" Text="Submit" runat="server" CssClass="styled-button" OnClick="btnSubmit_Click"/>
        </div>
    </form>
</body>
</html>
