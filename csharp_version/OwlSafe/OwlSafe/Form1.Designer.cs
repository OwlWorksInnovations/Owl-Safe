namespace OwlSafe
{
    partial class OwlSafe
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(OwlSafe));
            this.generateBox = new System.Windows.Forms.GroupBox();
            this.identifierInput = new System.Windows.Forms.TextBox();
            this.enterIdenetifierlbl = new System.Windows.Forms.Label();
            this.generateBtn = new System.Windows.Forms.Button();
            this.passwordLabel = new System.Windows.Forms.Label();
            this.copyBtn = new System.Windows.Forms.Button();
            this.searchBox = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.searchBtn = new System.Windows.Forms.Button();
            this.copyBtn1 = new System.Windows.Forms.Button();
            this.passwordSearchLabel = new System.Windows.Forms.Label();
            this.generateBox.SuspendLayout();
            this.searchBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // generateBox
            // 
            this.generateBox.Controls.Add(this.copyBtn);
            this.generateBox.Controls.Add(this.passwordLabel);
            this.generateBox.Controls.Add(this.generateBtn);
            this.generateBox.Controls.Add(this.identifierInput);
            this.generateBox.Controls.Add(this.enterIdenetifierlbl);
            this.generateBox.Location = new System.Drawing.Point(12, 12);
            this.generateBox.Name = "generateBox";
            this.generateBox.Size = new System.Drawing.Size(381, 426);
            this.generateBox.TabIndex = 0;
            this.generateBox.TabStop = false;
            this.generateBox.Text = "Generate";
            // 
            // identifierInput
            // 
            this.identifierInput.BackColor = System.Drawing.SystemColors.ActiveBorder;
            this.identifierInput.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.identifierInput.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.identifierInput.Location = new System.Drawing.Point(137, 16);
            this.identifierInput.Name = "identifierInput";
            this.identifierInput.Size = new System.Drawing.Size(141, 15);
            this.identifierInput.TabIndex = 3;
            this.identifierInput.TextChanged += new System.EventHandler(this.identifierInput_TextChanged);
            // 
            // enterIdenetifierlbl
            // 
            this.enterIdenetifierlbl.AutoSize = true;
            this.enterIdenetifierlbl.Location = new System.Drawing.Point(6, 16);
            this.enterIdenetifierlbl.Name = "enterIdenetifierlbl";
            this.enterIdenetifierlbl.Size = new System.Drawing.Size(125, 13);
            this.enterIdenetifierlbl.TabIndex = 2;
            this.enterIdenetifierlbl.Text = "Enter password identifier:";
            this.enterIdenetifierlbl.Click += new System.EventHandler(this.enterIdenetifierlbl_Click);
            // 
            // generateBtn
            // 
            this.generateBtn.Location = new System.Drawing.Point(98, 57);
            this.generateBtn.Name = "generateBtn";
            this.generateBtn.Size = new System.Drawing.Size(75, 23);
            this.generateBtn.TabIndex = 4;
            this.generateBtn.Text = "Generate";
            this.generateBtn.UseVisualStyleBackColor = true;
            this.generateBtn.Click += new System.EventHandler(this.generateBtn_Click);
            // 
            // passwordLabel
            // 
            this.passwordLabel.AutoSize = true;
            this.passwordLabel.Location = new System.Drawing.Point(6, 40);
            this.passwordLabel.Name = "passwordLabel";
            this.passwordLabel.Size = new System.Drawing.Size(53, 13);
            this.passwordLabel.TabIndex = 5;
            this.passwordLabel.Text = "Password";
            this.passwordLabel.Click += new System.EventHandler(this.passwordLabel_Click);
            // 
            // copyBtn
            // 
            this.copyBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 6F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.copyBtn.Location = new System.Drawing.Point(284, 15);
            this.copyBtn.Name = "copyBtn";
            this.copyBtn.Size = new System.Drawing.Size(56, 18);
            this.copyBtn.TabIndex = 6;
            this.copyBtn.Text = "COPY";
            this.copyBtn.UseVisualStyleBackColor = true;
            this.copyBtn.Click += new System.EventHandler(this.copyBtn_Click);
            // 
            // searchBox
            // 
            this.searchBox.Controls.Add(this.passwordSearchLabel);
            this.searchBox.Controls.Add(this.copyBtn1);
            this.searchBox.Controls.Add(this.searchBtn);
            this.searchBox.Controls.Add(this.textBox1);
            this.searchBox.Controls.Add(this.label1);
            this.searchBox.Location = new System.Drawing.Point(413, 12);
            this.searchBox.Name = "searchBox";
            this.searchBox.Size = new System.Drawing.Size(381, 426);
            this.searchBox.TabIndex = 7;
            this.searchBox.TabStop = false;
            this.searchBox.Text = "Search";
            this.searchBox.Enter += new System.EventHandler(this.searchBox_Enter);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(125, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Enter password identifier:";
            // 
            // textBox1
            // 
            this.textBox1.BackColor = System.Drawing.SystemColors.ActiveBorder;
            this.textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.textBox1.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox1.ForeColor = System.Drawing.SystemColors.WindowText;
            this.textBox1.Location = new System.Drawing.Point(137, 16);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(141, 15);
            this.textBox1.TabIndex = 1;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // searchBtn
            // 
            this.searchBtn.Location = new System.Drawing.Point(98, 54);
            this.searchBtn.Name = "searchBtn";
            this.searchBtn.Size = new System.Drawing.Size(75, 23);
            this.searchBtn.TabIndex = 2;
            this.searchBtn.Text = "Search";
            this.searchBtn.UseVisualStyleBackColor = true;
            this.searchBtn.Click += new System.EventHandler(this.searchBtn_Click);
            // 
            // copyBtn1
            // 
            this.copyBtn1.Font = new System.Drawing.Font("Microsoft Sans Serif", 6F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.copyBtn1.Location = new System.Drawing.Point(284, 16);
            this.copyBtn1.Name = "copyBtn1";
            this.copyBtn1.Size = new System.Drawing.Size(56, 17);
            this.copyBtn1.TabIndex = 3;
            this.copyBtn1.Text = "COPY";
            this.copyBtn1.UseVisualStyleBackColor = true;
            this.copyBtn1.Click += new System.EventHandler(this.copyBtn1_Click);
            // 
            // passwordSearchLabel
            // 
            this.passwordSearchLabel.AutoSize = true;
            this.passwordSearchLabel.Location = new System.Drawing.Point(6, 42);
            this.passwordSearchLabel.Name = "passwordSearchLabel";
            this.passwordSearchLabel.Size = new System.Drawing.Size(53, 13);
            this.passwordSearchLabel.TabIndex = 8;
            this.passwordSearchLabel.Text = "Password";
            this.passwordSearchLabel.Click += new System.EventHandler(this.passwordSearchLabel_Click);
            // 
            // OwlSafe
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.searchBox);
            this.Controls.Add(this.generateBox);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "OwlSafe";
            this.Text = "Owl Safe";
            this.generateBox.ResumeLayout(false);
            this.generateBox.PerformLayout();
            this.searchBox.ResumeLayout(false);
            this.searchBox.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox generateBox;
        private System.Windows.Forms.TextBox identifierInput;
        private System.Windows.Forms.Label enterIdenetifierlbl;
        private System.Windows.Forms.Button generateBtn;
        private System.Windows.Forms.Label passwordLabel;
        private System.Windows.Forms.Button copyBtn;
        private System.Windows.Forms.GroupBox searchBox;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button searchBtn;
        private System.Windows.Forms.Button copyBtn1;
        private System.Windows.Forms.Label passwordSearchLabel;
    }
}

