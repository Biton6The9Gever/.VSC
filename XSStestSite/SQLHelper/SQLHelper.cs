using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;

/// <summary>
/// Description: Sql helper methods
/// Class Name: SQLHelper
/// Author: Tzali Gershgoren
/// Date: 19/11/2015
/// </summary>
public class SQLHelper
{
    #region Public Static Memebrs
    /// <summary>
    /// Connection string
    /// </summary>
    public static string connectionString = ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
    #endregion

    #region Public Static Methods
    /// <summary>
    /// Returns a datatable using the provided sql query sql.
    /// </summary>
    /// <param name="sql"></param>
    /// <returns>Datatable with the content from the DB</returns>
    public static DataTable SelectData(string sql)
    {
        DataTable table = new DataTable();
        //create new connection to the db file
        using (SqlConnection conn = new SqlConnection(SQLHelper.connectionString))
        {
            //create new object for the query execution
            using (SqlCommand comm = new SqlCommand(sql, conn))
            {
                try
                {
                    //open connection with the DB - פתיחת הקישור לבסיס הנתונים 
                    conn.Open();
                    comm.CommandTimeout = 0;
                    ///execute the query -  ביצוע שאלתא
                    SqlDataReader reader = comm.ExecuteReader();
                    //load the data table
                    table.Load(reader);
                }
                catch (Exception exp)
                {
                    SQLHelper.ErrorBox(exp, "Error while performing sql command", comm.CommandText, "");

                }
                finally
                {
                    //close connection -  סגירת הקישור לבסיס הנתונים
                    conn.Close();
                }
            }
        }
        return table;
    }

    /// <summary>
    /// Returns number of affected rows using the provided sql query srting.
    /// </summary>
    /// <param name="sql">The sql qurey to execute</param>
    /// <returns>The affected rows count</returns>
    public static int DoQuery(string sql)
    {
        int rows = 0;
        // create new connection to the db file
        using (SqlConnection conn = new SqlConnection(SQLHelper.connectionString))
        {
            //create new object for the query execution
            using (SqlCommand comm = new SqlCommand(sql, conn))
            {
                try
                {
                    //open connection with the DB - פתיחת הקישור לבסיס הנתונים 
                    conn.Open();
                    //execute query
                    rows = comm.ExecuteNonQuery();
                }
                catch (Exception exp)
                {
                    SQLHelper.ErrorBox(exp, "Error while performing sql command", comm.CommandText, "");
                }
                finally
                {
                    //close connection -  סגירת הקישור לבסיס הנתונים
                    conn.Close();
                }
            }
        }
        return rows;
    }

    /// <summary>
    /// Returns a scalar using the provided sql query.
    /// </summary>
    /// <param name="sql">The sql qurey to execute </param>
    /// <returns>The scalar object</returns>
    public static object SelectScalar(string sql)
    {
        object scalar = null;
        //create new connection to the db file
        using (SqlConnection conn = new SqlConnection(SQLHelper.connectionString))
        {
            //create new object for the query execution
            using (SqlCommand comm = new SqlCommand(sql, conn))
            {
                try
                {
                    //open connection with the DB
                    conn.Open();
                    //execute the query (scalar) - ביצוע השאילתא
                    scalar = comm.ExecuteScalar();
                }
                catch (Exception exp)
                {
                    //log the exception
                    SQLHelper.ErrorBox(exp, "Error while performing sql command", comm.CommandText, "");
                }
                finally
                {
                    //close connection -  סגירת הקישור לבסיס הנתונים
                    conn.Close();
                }
            }
        }
        return scalar;
    }


    /// <summary>
    /// Returns an int value from a scalar SQL command         
    /// </summary>
    /// <param name="sql">The sql qurey to execute</param>        
    /// <returns>the scalar execution converted to int</returns>
    public static int SelectScalarToInt32(string sql)
    {
        object obj = SelectScalar(sql);
        return Convert.ToInt32(obj);
    }

    /// <summary>
    /// Returns a double value from a scalar SQL command         
    /// </summary>
    /// <param name="sql">The sql qurey to execute</param>        
    /// <returns>the scalar execution converted to double</returns>
    public static double SelectScalarToDouble(string sql)
    {
        object obj = SelectScalar(sql);
        return Convert.ToDouble(obj);
    }


    /// <summary>
    /// execute scalar to string
    /// </summary>
    /// <param name="sql">The sql qurey to execute</param>        
    /// <returns>the scalar execution converted to string</returns>
    public static string SelectScalarToString(string sql)
    {
        object obj = SelectScalar(sql);
        return Convert.ToString(obj);
    }

    /// <summary>
    /// execute scalar to bool
    /// </summary>
    /// <param name="sql">The sql qurey to execute</param>        
    /// <returns>the scalar execution converted to boolean</returns>
    public static bool SelectScalarToBool(string sql)
    {
        object obj = SelectScalar(sql);
        return Convert.ToBoolean(obj);
    }


    /// <summary>
    /// Pop up error box
    /// </summary>
    /// <param name="exp">the original expeption </param>
    /// <param name="message">the error message</param>
    /// <param name="methodName">the method which threw the exeption</param>
    /// <param name="additionalData">additional data string</param>
    public static void ErrorBox(Exception exp,
        string message, string methodName,
        string additionalData)
    {
        //TODO - log to file system/db/email/etc.            
    }
    #endregion
}

