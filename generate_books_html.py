import json

def generate_books_html(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    html_content = '''<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Books</title>
    <link rel="stylesheet" href="/css/aboutStylesheet.css" type="text/css" />
    <style>
      .download-link {
        display: inline-block;
        margin: 10px 0;
        padding: 10px 20px;
        background-color: #757d5f; /* Match color of project containers */
        color: #e0dcc5; /* Match text color of project containers */
        text-decoration: none;
        border-radius: 4px;
        transition: background-color 0.3s, color 0.3s;
        width: 100%;
        text-align: center;
      }
      .download-link:hover {
        background-color: #e0dcc5; /* Match hover color of project containers */
        color: #757d5f; /* Match text color on hover */
      }
      .subject h2 {
        color: #3a5a40; /* Dark green color for subject titles */
      }
      .contact-form,
      #password-container {
        margin: 20px auto;
        max-width: 600px;
        padding: 20px;
        background-color: #e0dcc5; /* Match background color */
        border-radius: 8px;
        color: #3a5a40; /* Match text color */
      }
      .contact-form h2,
      #password-container h2 {
        color: #3a5a40; /* Match header color */
        text-align: center;
        margin: 0; /* Remove outline around header */
      }
      .contact-form label,
      .contact-form input,
      .contact-form textarea,
      #password-container input,
      #password-container button {
        display: block;
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #757d5f; /* Match border color */
        border-radius: 4px;
        color: #3a5a40; /* Match text color */
        outline: none; /* Remove outline */
      }
      #password-container label,
      .contact-form label {
        display: block;
        width: 100%;
        padding-top: 10px;
        padding-bottom: 10px;
        margin-bottom: 10px;
        color: #3a5a40; /* Match text color */
        outline: none; /* Remove outline */
        border: none; /* Ensure no border */
      }
      .contact-form input[type="submit"],
      #password-container button {
        background-color: #757d5f; /* Match button color */
        color: #e0dcc5; /* Match button text color */
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
      }
      .contact-form input[type="submit"]:hover,
      #password-container button:hover {
        background-color: #3a5a40; /* Match button hover color */
      }
      .page-header .title {
        text-align: center;
      }
      .download-link-container {
        width: 100%;
        display: flex;
        justify-content: center;
      }
    </style>
    <script
      type="text/javascript"
      src="/javascript/typekit.js"
      async
      onload="try { window.Typekit.load(); } catch (e) { console.warn('Typekit not loaded.'); }"
    ></script>
    <script>
      function sendEmail(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;
        window.location.href = `mailto:sullivan.hart7@gmail.com?subject=Contact from ${name}&body=Email: ${email}%0D%0A%0D%0A${message}`;
      }
    </script>
  </head>
  <body class="transition-enabled">
    <div id="password-container">
      <h2>Enter Password</h2>
      <label for="password-input">Password:</label>
      <input type="password" id="password-input" />
      <button onclick="checkPassword()">Submit</button>
      <p id="error-message" style="color: red; display: none">
        Incorrect password. Please try again.
      </p>
    </div>
    <div id="content-container" style="display: none">
      <div class="site-wrap cfix">
        <div class="site-container">
          <div class="site-content e2e-site-content">
            <header
              class="site-header js-site-header"
              data-context="theme.nav"
              data-hover-hint="nav"
              data-hover-hint-placement="top-start"
            >
              <nav
                class="nav-container"
                data-hover-hint="nav"
                data-hover-hint-placement="bottom-start"
              >
                <div class="page-title">
                  <a href="/">MAIN</a>
                </div>
                <div class="page-title">
                  <a href="/images/Resume/Resume.pdf" target="_blank">RESUME</a>
                </div>
                <div class="page-title">
                  <a href="/about.html">ABOUT ME</a>
                </div>
                <div class="page-title">
                  <a href="/previous-experience.html">PREVIOUS EXPERIENCE</a>
                </div>
                <div class="page-title">
                  <a href="/classes.html">CLASSES</a>
                </div>
                <div class="gallery-title">
                  <a href="/projects.html">PROJECTS</a>
                </div>
                <div class="page-title">
                  <a href="/mandatory.html">CPRE 494</a>
                </div>
              </nav>
              <div
                class="logo-wrap"
                data-context="theme.logo.header"
                data-hover-hint="logo"
                data-hover-hint-placement="bottom-start"
              >
                <div class="logo e2e-site-logo-text logo-text">
                  <a href="/" class="preserve-whitespace">SULLIVAN HART</a>
                </div>
              </div>
              <a href="/nav.html">
                <div class="hamburger-click-area js-hamburger">
                  <div class="hamburger">
                    <i></i>
                    <i></i>
                    <i></i>
                  </div>
                </div>
              </a>
            </header>
            <main>
              <div
                class="page-container js-site-wrap"
                data-context="page.page.container"
                data-hover-hint="pageContainer"
              >
                <section class="page standard-modules">
                  <header
                    class="page-header content"
                    data-context="pages"
                    data-identity="id:p656e077c9ccd095a66ee1ec852067cf2a442d8d82c49b88fd4f70"
                    data-hover-hint="pageHeader"
                    data-hover-hint-id="p656e077c9ccd095a66ee1ec852067cf2a442d8d82c49b88fd4f70"
                  >
                    <h1 class="title preserve-whitespace e2e-site-logo-text">
                      Books
                    </h1>
                  </header>
                  <div
                    class="page-content js-page-content"
                    data-context="pages"
                    data-identity="id:p656e077c9ccd095a66ee1ec852067cf2a442d8d82c49b88fd4f70"
                  >
                    <div
                      id="project-canvas"
                      class="js-project-modules modules content"
                    >
                      <div id="books-container">
    '''

    for subject, books in data.items():
        html_content += f'''
                        <div class="subject">
                          <h2>{subject}</h2>
        '''
        for book in books:
            html_content += f'''
                          <div class="download-link-container">
                            <a
                              href="{book['url']}"
                              class="download-link"
                              download
                              >Download {book['title']}</a
                            >
                          </div>
            '''
        html_content += '''
                        </div>
        '''

    html_content += '''
                      </div>
                    </div>
                  </div>
                </section>
                <section class="contact-form-section">
                  <div class="contact-form">
                    <h2 class="title preserve-whitespace e2e-site-logo-text">Contact Me</h2>
                    <br />
                    <p style="text-align: center; color: #3a5a40;">Please contact me for book requests or takedown notices.</p>
                    <br />
                    <form onsubmit="sendEmail(event)">
                      <label for="name">Name:</label>
                      <input type="text" id="name" name="name" required />
                      <label for="email">Email:</label>
                      <input type="email" id="email" name="email" required />
                      <label for="message">Message:</label>
                      <textarea
                        id="message"
                        name="message"
                        rows="4"
                        required
                      ></textarea>
                      <input type="submit" value="Send" />
                    </form>
                  </div>
                </section>
              </div>
            </main>
          </div>
            <footer class="site-footer" data-hover-hint="footer">
              <div class="footer-text">
                <p>
                  <a href="mailto:hartsul@iastate.edu" target="_blank"
                    >hartsul@iastate.edu</a
                  >
                </p>
                <p>(952) 913-4006</p>
                <p>
                  <a
                    href="https://www.linkedin.com/in/sullivan-hart/"
                    target="_blank"
                    >LinkedIn</a
                  >
                </p>
                <p>
                  <a href="https://github.com/SullivanHart" target="_blank"
                    >GitHub</a
                  >
                </p>
              </div>
            </footer>
          </div>
        </div>
      </div>
    </div>
    <script type="text/javascript">
      // fix for Safari's back/forward cache
      window.onpageshow = function (e) {
        if (e.persisted) {
          window.location.reload();
        }
      };

      function checkPassword() {
        const password = document
          .getElementById("password-input")
          .value.toLowerCase();
        if (password === "books") {
          document.getElementById("password-container").style.display = "none";
          document.getElementById("content-container").style.display = "block";
        } else {
          document.getElementById("error-message").style.display = "block";
        }
      }
    </script>
  </body>
</html>
    '''

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_books_html('books.json', 'books.html')
