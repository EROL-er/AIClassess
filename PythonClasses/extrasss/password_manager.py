# password_manager.py

class BasePasswordManager:
    """
    Holds all old passwords; the last item is the current password.
    """
    def __init__(self):
        self.old_passwords = []  # type: list[str]

    def get_password(self) -> str | None:
        """Return the current password (or None if not set)."""
        return self.old_passwords[-1] if self.old_passwords else None

    def is_correct(self, candidate: str) -> bool:
        """True if candidate equals current password, else False."""
        current = self.get_password()
        return current is not None and candidate == current


class PasswordManager(BasePasswordManager):
    """
    Inherits BasePasswordManager and enforces:
      - min length 6
      - can set first password if length is OK
      - otherwise, new password level must be greater than current level
      - if current is already highest level (2), new must also be level 2
    """

    def get_level(self, password: str | None = None) -> int:
        """
        Security levels:
          0: only letters OR only digits
          1: alphanumeric (letters and digits only, no specials)
          2: contains any special character (non-alphanumeric)
        """
        if password is None:
            password = self.get_password() or ""

        has_letter = any(ch.isalpha() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)
        has_special = any(not ch.isalnum() for ch in password)

        if has_special:
            return 2
        if has_letter and has_digit:
            return 1
        return 0  # only letters OR only digits

    def set_password(self, new_password: str) -> bool:
        """
        Attempt to set the user's password.
        Returns True on success, False on failure.
        Rules:
          - length >= 6
          - if no current password, accept (length rule still applies)
          - else require new_level > current_level
          - if current_level == 2, require new_level == 2
        """
        if not isinstance(new_password, str):
            return False
        if len(new_password) < 6:
            return False

        current = self.get_password()
        new_level = self.get_level(new_password)

        # First-time set
        if current is None:
            self.old_passwords.append(new_password)
            return True

        current_level = self.get_level(current)

        # If current is already highest level, new must also be highest
        if current_level == 2:
            if new_level == 2:
                self.old_passwords.append(new_password)
                return True
            return False

        # Otherwise, new must be strictly greater level
        if new_level > current_level:
            self.old_passwords.append(new_password)
            return True

        return False


# ---------------------------
# Minimal usage demo (remove if importing as a module)
if __name__ == "__main__":
    pm = PasswordManager()

    # First set: must be length >= 6
    print(pm.set_password("secret1"))        # True (level 1: letters+digits)
    print(pm.get_password(), pm.get_level()) # secret1, 1

    # Won't allow same or lower level than current (1)
    print(pm.set_password("letters"))        # False (level 0, lower)
    print(pm.set_password("1234567"))        # False (level 0, lower)

    # Allow higher level (to 2: includes special)
    print(pm.set_password("S3cret!"))        # True (level 2)
    print(pm.get_password(), pm.get_level()) # S3cret!, 2

    # Now current is highest level; only another level-2 is allowed
    print(pm.set_password("newpass"))        # False (level 0)
    print(pm.set_password("NewP4ss#"))       # True (level 2)

    # Check correctness
    print(pm.is_correct("NewP4ss#"))         # True
    print(pm.is_correct("wrong"))            # False

    # Old passwords list (last one is current)
    print(pm.old_passwords)
