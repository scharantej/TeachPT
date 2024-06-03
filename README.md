## Flask Application Design for Building a Website that Teaches Portuguese

### HTML Files
- **index.html**:
 >- Serves as the main home page of the website.
 >- Contains links to different Portuguese learning sections.

### Routes
- **@app.route('/')**:
 >- This route is mapped to the home page, 'index.html'.
 >- When a user visits the website's root URL (http://localhost:5000/), this route will render 'index.html'.

- **@app.route('/grammar')**:
 >- This route handles the Portuguese grammar section.
 >- When a user clicks on the grammar link in 'index.html', this route will serve a separate HTML template ('grammar.html') dedicated to grammar lessons.

- **@app.route('/vocabulary')**:
 >- This route handles the Portuguese vocabulary section.
 >- Similar to the grammar section, when a user clicks on the vocabulary link in 'index.html', this route renders 'vocabulary.html', which focuses on vocabulary building.

- **@app.route('/exercises')**:
 >- This route serves the exercises section.
 >- When a user accesses the exercises link in 'index.html', this route provides 'exercises.html', which contains interactive exercises to test the user's Portuguese skills.

- **@app.route('/about')**:
 >- This route displays the 'about' page.
 >- When a user clicks on the 'About' link in 'index.html', this route serves 'about.html', providing information about the website's purpose, creators, etc.