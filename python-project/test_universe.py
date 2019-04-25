from universe import est_majeur
import builtins


sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_est_majeur():
    try:
        result = est_majeur(1)
        assert result == False, "Running est_majeur(1))... Expected False, got {}".format(result)
        result = est_majeur(20)
        assert result == True, "Running est_majeur(20))... Expected True, got {}".format(result)
        success()

        if sum_builtin_used:
            send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
            send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
            send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
            send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
            send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
            send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
            send_msg("My personal Yoda, you are. 🙏", "_)_/LI")
        else:
            send_msg("Kudos 🌟", "Did you know that you could use the sum function? Try it!")
            send_msg("Kudos 🌟", "")
            send_msg("Kudos 🌟", "galaxies = [37, 3, 2]")
            send_msg("Kudos 🌟", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    test_est_majeur()
