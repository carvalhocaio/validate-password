class Password:
    def __init__(self, body):
        self.password = body["password"]
        self.rules = body["rules"]

        self.minSize = None
        self.minUppercase = None
        self.minLowercase = None
        self.minDigit = None
        self.minSpecialChars = None
        self.noRepeted = None

        self.noMatch = list()
        self.verify_password = False

    def define_rules(self, rules):
        if self.rules:
            for rule in rules:
                match rule["rule"]:
                    case "minSize":
                        self.minSize = rule["value"]
                    case "minUppercase":
                        self.minUppercase = rule["value"]
                    case "minLowercase":
                        self.minLowercase = rule["value"]
                    case "minDigit":
                        self.minDigit = rule["value"]
                    case "minSpecialChars":
                        self.minSpecialChars = rule["value"]
                    case "noRepeted":
                        self.noRepeted = rule["value"]

    def verify_password_min_size(self):
        if self.minSize:
            if len(self.password) < self.minSize:
                self.noMatch.append("minSize")

    def verify_password_min_uppercase(self):
        if self.minUppercase:
            countUpper = 0
            for i in self.password:
                if i.isupper():
                    countUpper += 1

            if countUpper < self.minUppercase:
                self.noMatch.append("minUppercase")

    def verify_password_min_lowercase(self):
        if self.minLowercase:
            countLower = 0
            for i in self.password:
                if i.islower():
                    countLower += 1

            if countLower < self.minLowercase:
                self.noMatch.append("minLowercase")

    def verify_password_min_digit(self):
        if self.minDigit:
            countDigit = 0
            for i in self.password:
                if i.isnumeric():
                    countDigit += 1

            if countDigit < self.minDigit:
                self.noMatch.append("minDigit")

    def verify_password_min_special_chars(self):
        special_chars = "!@#$%^&*()-+\/{}[]"

        if self.minSpecialChars:
            countSpecialChars = 0
            for i in self.password:
                if i in special_chars:
                    countSpecialChars += 1

            if countSpecialChars < self.minSpecialChars:
                self.noMatch.append("minSpecialChars")

    def verify_password_no_repeted(self):
        if self.noRepeted == 0:
            if any(
                letter == self.password[idx + 1]
                for idx, letter in enumerate(self.password[:-1])
            ):
                self.noMatch.append("noRepeted")

    def verify(self):
        self.define_rules(self.rules)

        self.verify_password_min_size()
        self.verify_password_min_uppercase()
        self.verify_password_min_lowercase()
        self.verify_password_min_digit()
        self.verify_password_min_special_chars()
        self.verify_password_no_repeted()

        if not self.noMatch:
            self.verify_password = True

        return self.verify_password, self.noMatch
