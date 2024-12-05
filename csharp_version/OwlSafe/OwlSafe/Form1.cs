using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows;
using System.IO;

namespace OwlSafe
{
    public partial class OwlSafe : Form
    {
        public OwlSafe()
        {
            InitializeComponent();
            passwordLabel.Text = "";
            passwordSearchLabel.Text = "";
        }
        string appPath = AppDomain.CurrentDomain.BaseDirectory;
        private void enterIdenetifierlbl_Click(object sender, EventArgs e)
        {

        }
        private void identifierInput_TextChanged(object sender, EventArgs e)
        {

        }

        private void generateBtn_Click(object sender, EventArgs e)
        {
            string generate_password(int length)
            {
                Random res = new Random();
                string CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=";
                string ran = "";

                for (int i = 0; i < length; i++)
                {
                    int x = res.Next(CHARACTERS.Length);
                    ran += CHARACTERS[x];
                }

                return ran;
            }

            string save_password(string path, string identifier, string password)
            {
                using (StreamWriter outputFile = new StreamWriter(Path.Combine(path, "password.txt"), true))
                {
                    outputFile.WriteLine(identifier + "," + password);
                }
                return path;
            }

            if (string.IsNullOrEmpty(identifierInput.Text))
            {
                passwordLabel.Text = "Identifier cannot be empty!";
                return;
            }
            else
            {
                string randomPassword = generate_password(12);

                bool identifierExists = false;

                string[] lines = File.Exists(Path.Combine(appPath, "password.txt"))
                    ? File.ReadAllLines(Path.Combine(appPath, "password.txt"))
                    : new string[0];

                foreach (string line in lines)
                {
                    string[] formattedIdentifier = line.Split(',');
                    if (formattedIdentifier[0] == identifierInput.Text)
                    {
                        identifierExists = true;
                        break;
                    }
                }

                if (identifierExists)
                {
                    passwordLabel.Text = "Identifier already exists!";
                }
                else
                {
                    save_password(appPath, identifierInput.Text, randomPassword);
                    passwordLabel.Text = randomPassword;
                }
            }
        }


        private void passwordLabel_Click(object sender, EventArgs e)
        {
            if (identifierInput.Text != "")
                Clipboard.SetText(passwordLabel.Text);
        }

        private void copyBtn_Click(object sender, EventArgs e)
        {
            if (identifierInput.Text != "")
                Clipboard.SetText(passwordLabel.Text);
        }

        private void searchBox_Enter(object sender, EventArgs e)
        {

        }

        private void copyBtn1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
                Clipboard.SetText(passwordSearchLabel.Text);
        }

        private void passwordSearchLabel_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
                Clipboard.SetText(passwordSearchLabel.Text);
        }

        private void searchBtn_Click(object sender, EventArgs e)
        {
            string search_password(string identifier, string path)
            {
                using (StreamReader reader = new StreamReader(Path.Combine(path, "password.txt")))
                {
                    string line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        string[] parts = line.Split(',');
                        if (parts[0] == identifier)
                        {
                            return parts[1];
                        }
                    }
                }
                return null;
            }


            // Visual Studio recommended me this way
            if (!string.IsNullOrEmpty(textBox1.Text))
            {
                string password = search_password(textBox1.Text, appPath);

                passwordSearchLabel.Text = password;
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
