def mutate(string, position, character):
    string=(list(string))
    string[position]=character
    final=' '.join(string)
    return final