from collections import defaultdict

class VersionHistory:
    def __init__(self, content):
        self.versions = defaultdict(str)
        self.cur_version = 1
        self.versions[self.cur_version] = content

    def save(self, content):
        self.cur_version += 1
        self.versions[self.cur_version] = content
        return self.cur_version
    
    def get(self, version):
        if version > self.cur_version or version < 1:
            raise IndexError(f"Version does not exist with ID={version}")
        return self.versions[version]
    
    def revert(self, version):
        if version > self.cur_version or version < 1:
            raise IndexError(f"Version does not exist with ID={version}")
        self.save(self.versions[version])
        return self.cur_version

    def diff(self, version1, version2):
        # pass in two version ids, return line changes (split lines)

        version1_content = self.get(version1)
        version2_content = self.get(version2)

        version1_set = set(version1_content.splitlines())
        version2_set = set(version2_content.splitlines())

        difference = sorted(['-' + lines for lines in (version1_set - version2_set)])
        difference += sorted(['+' + lines for lines in (version2_set - version1_set)])
        
        return difference
    
    def history(self):
        return [(version, content) for version, content in self.versions.items()]


vh = VersionHistory("Hello world")
print(vh.save("Hello world\nNew line"))   # → 2
# print(vh.get(0))
# print(vh.get(3))
print(vh.save("Goodbye world"))           # → 3

print(vh.get(1))       # → "Hello world"
print(vh.get(2))       # → "Hello world\nNew line"

print(vh.diff(1, 2))   # → ["+New line"]
print(vh.diff(2, 3))   # → ["-Hello world", "-New line", "+Goodbye world"]

print(vh.revert(1))    # → 4  (creates a new version with content of v1)
print(vh.get(4))       # → "Hello world"

print(vh.history())    # → [(1, "Hello world"), (2, "Hello world\nNew line"),
                #    (3, "Goodbye world"), (4, "Hello world")]



