from collections import defaultdict

class TagSystem:
    def __init__(self):
        self.docs_map = defaultdict(set) # tags in set, doc is key
        self.tags_map = defaultdict(set) # docs in set, tag is key

    def add_tag(self, doc, tag):
        self.docs_map[doc].add(tag)
        self.tags_map[tag].add(doc)
    
    def remove_tag(self, doc, tag):
        if tag not in self.docs_map.get(doc, set()):
            raise ValueError

        self.docs_map[doc].remove(tag)
        self.tags_map[tag].remove(doc)
        
    def get_tags(self, doc):
        return sorted(self.docs_map.get(doc, set()))
    
    def get_docs(self, tag):
        return sorted(self.tags_map.get(tag, set()))
    
    def get_related(self, doc):
        if doc not in self.docs_map:
            raise ValueError
        
        related_tags = self.docs_map[doc]
        return_set = set()
        for t in related_tags:
            for d in self.tags_map[t]:
                return_set.add(d)

        return_set.remove(doc)
        return sorted(return_set)
    
ts = TagSystem()
ts.add_tag("page1", "python")
ts.add_tag("page1", "backend")
ts.add_tag("page2", "python")
ts.add_tag("page2", "frontend")
ts.add_tag("page3", "backend")

print(ts.get_tags("page1"))        # → ["backend", "python"]
print(ts.get_docs("python"))       # → ["page1", "page2"]
print(ts.get_related("page1"))     # → ["page2", "page3"]
                            # page2 shares "python", page3 shares "backend"

ts.remove_tag("page1", "python")
print(ts.get_related("page1"))     # → ["page3"]  (only "backend" tag remains)
ts.remove_tag("page1", "java")  # → raises ValueError


    
