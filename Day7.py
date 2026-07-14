# This is a set of programming skills

skill = {"python", "java", "c++", "javascript", "html", "css", "sql", "css", "php", "swift"}

print("My skills are:" , skill)

required_skills = {"python", "java", "c++", "TypeScript"}
print("Required skills are:" , required_skills)

common_skills = skill & required_skills
print("Common skills are:" , common_skills) 

frozen_skills = frozenset(skill)
print("Frozen skills are:" , frozen_skills)

common_frozen_skills = frozen_skills & required_skills
print("Common frozen skills are:" , common_frozen_skills)

print("The value of skill")
for i in skill:
    print(i)

print("The value of frozenskill")
for i in frozen_skills:
    print(i)    