using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Windows.Forms;

namespace OwlSafe
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string userInput = txtInput.Text.Trim();
            int passwordLength = 12;
            // Make this flexible by making it automatically creating the file if it does not exist and find the current directory
            string passwordFile = "C:\\Users\\juanp\\source\\repos\\OwlSafe\\OwlSafe\\bin\\Debug\\storage\\password.txt";

            if (string.IsNullOrWhiteSpace(userInput))
            {
                label2.Text = "Identifier cannot be empty.";
                return;
            }

            string GenerateRandomPassword(int length)
            {
                List<char> characters = new List<char> {
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '='
                };

                Random random = new Random();
                StringBuilder sb = new StringBuilder();

                for (int i = 0; i < length; i++)
                {
                    char randomChar = characters[random.Next(characters.Count)];
                    sb.Append(randomChar);
                }

                return sb.ToString();
            }


            string randomPassword = GenerateRandomPassword(passwordLength);

            if (File.Exists(passwordFile))
            {
                Dictionary<string, string> passwordData = new Dictionary<string, string>();
                foreach (var line in File.ReadLines(passwordFile))
                {
                    var parts = line.Split(',');
                    if (parts.Length == 2)
                    {
                        passwordData[parts[0]] = parts[1];
                    }
                }
                if (passwordData.ContainsKey(userInput))
                {
                    label2.Text = "Identifier already exists.";
                    return;
                }
            }
            string newEntry = $"{userInput},{randomPassword}";
            File.AppendAllText(passwordFile, newEntry + Environment.NewLine);
            label2.Text = "Random password: " + randomPassword;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Show panel1 and hide panel2
            panel1.Visible = true;
            panel2.Visible = false;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // Show panel2 and hide panel1
            panel2.Visible = true;
            panel1.Visible = false;
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {
            // Custom painting logic for panel2, if needed
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            // Custom painting logic for panel1, if needed
        }
        private void lblOutput_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            string userInputSearch = textBox1.Text.Trim();
            string passwordFile = "C:\\Users\\juanp\\source\\repos\\OwlSafe\\OwlSafe\\bin\\Debug\\storage\\password.txt";

            void SearchWord(string searchWord)
            {
                if (File.Exists(passwordFile))
                {
                    foreach (var line in File.ReadLines(passwordFile))
                    {
                        var parts = line.Split(',');
                        if (parts.Length == 2)
                        {
                            if (parts[0].Trim() == searchWord)
                            {
                                label4.Text = parts[1].Trim(); // Display word after the comma
                                return;
                            }
                        }
                    }

                    label4.Text = "Not found."; // If no match is found
                }
                else
                {
                    label4.Text = "File not found."; // If file doesn't exist
                }
            }

            SearchWord(userInputSearch);
        }
    }
}
