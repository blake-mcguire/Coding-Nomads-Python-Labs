# Fix the wikipedia blurb below by replacing the value for `animal`
# with the name of the animal that the text is talking about.
# Then, change the that way you're displaying the multi-line string
# so that the output doesn't show any superfluous spacing.

animal = "cat"
blurb = f"The {animal} (Felis {animal}us) is a domestic species of small \ncarnivorous mammal. It is the only domestic{animal}ed species \n in the family Felidae and is often referred to as the \n domestic {animal} to distinguish it from the wild members of the family."

print(blurb)