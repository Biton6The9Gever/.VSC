using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace XSStestSite
{
    public partial class _01LoginPage : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            // Fetching username and password input from text boxes
            string username = txtUsername.Text;
            string password = txtPassword.Text;

            // Creating SQL query that directly uses user input without parameterization
            string query = $"SELECT Username FROM Users WHERE [Username] = '{username}' AND [Password] = '{password}';";

            // Using the SQLHelper to execute the query
            DataTable result = SQLHelper.SelectData(query);

            if (result.Rows.Count > 0)
            {
                // User exists; login successful
                Response.Redirect("02HomePage.aspx");
            }
            else
            {
                // User not found; login failed
                ClientScript.RegisterStartupScript(this.GetType(), "alert", "alert('Invalid username or password.');", true);
            }
        }
    }
}