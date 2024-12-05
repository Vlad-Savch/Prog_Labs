class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"{self.name} ({self.age})"


class AgeGroup:
    def __init__(self, lower_bound, upper_bound=None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def sort_respondents(self):
        self.respondents.sort(key=lambda r: (-r.age, r.name))

    def __str__(self):
        if self.upper_bound:
            group_name = f"{self.lower_bound}-{self.upper_bound}"
        else:
            group_name = f"{self.lower_bound}+"

        respondents_str = ", ".join(str(r) for r in self.respondents)
        return f"{group_name}: {respondents_str}"


class SurveyProcessor:
    def __init__(self, age_boundaries):
        self.age_boundaries = sorted(map(int, age_boundaries))
        self.groups = self.create_groups()

    def create_groups(self):
        groups = []
        for i in range(len(self.age_boundaries) - 1):
            groups.append(AgeGroup(self.age_boundaries[i] + 1, self.age_boundaries[i + 1]))
        groups.append(AgeGroup(self.age_boundaries[-1] + 1))
        return groups[::-1]

    def assign_to_groups(self, respondents):
        for respondent in respondents:
            for group in self.groups:
                if (group.upper_bound and group.lower_bound <= respondent.age <= group.upper_bound) or \
                        (not group.upper_bound and respondent.age >= group.lower_bound):
                    group.add_respondent(respondent)
                    break

    def print_results(self):
        for group in self.groups:
            group.sort_respondents()
            if group.respondents:
                print(group)


def main():
    import sys
    age_boundaries = sys.argv[1:]

    processor = SurveyProcessor(age_boundaries)

    respondents = []
    while True:
        line = input()
        if line == "END":
            break
        name, age = line.split(",")
        respondents.append(Respondent(name.strip(), int(age.strip())))

    processor.assign_to_groups(respondents)
    processor.print_results()


if __name__ == "__main__":
    main()
