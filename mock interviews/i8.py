class BrowserHistory:

    def __init__(self, homepage):
        self.stack = [homepage]
        self.visiting = 0

    def visit(self, url):
        while self.visiting < len(self.stack) - 1:
            self.stack.pop()
        
        self.stack.append(url)
        self.visiting = len(self.stack) - 1

    def back(self, steps):
        while steps > 0 and self.visiting > 0:
            self.visiting -= 1
            steps -= 1
        
        return self.stack[self.visiting]
    
    def forward(self, steps):
        while steps > 0 and self.visiting < len(self.stack) - 1:
            self.visiting += 1
            steps -= 1
        
        return self.stack[self.visiting]

    def current(self):
        return self.stack[self.visiting]

    def history(self):
        res = []

        for index, page in enumerate(self.stack):
            if index == self.visiting:
                res.append('*' + page)
            else:
                res.append(page)

        return res

bh = BrowserHistory("home")
bh.visit("about")
print(bh.visit("blog"))
print(bh.visit("contact"))

print(bh.back(1))      # → "blog"
print(bh.back(2))      # → "home"   (only 2 steps available, not 3)
print(bh.forward(1))   # → "about"
print(bh.visit("docs"))  # clears forward history

print(bh.forward(10))  # → "docs"   (no forward history)
print(bh.back(1))      # → "about"

print(bh.history())
# → ["home", "*about", "docs"]
#   (blog and contact were cleared when "docs" was visited)
