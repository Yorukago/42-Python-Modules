import sys

"""
what if u cant use print? sys.stdout.write works well too
in the amazing world of file descriptors, theres stdin, stdout and stderr
same in here! still u wouldnt really mix prints with stdin, out or err...
sooo yeah tbh idk why would someone use this besides making a very, very
annoying program... unless u wanna send shit to stderr...??
"""


def run_comms_test() -> None:
    archivist_id: str = input("\nInput Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")
    standard_msg: str = (
        f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    )
    sys.stdout.write(standard_msg)
    alert_msg: str = (
        "[ALERT] System diagnostic: "
        "Communication channels verified\n"
    )
    sys.stderr.write(alert_msg)

    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")


def main() -> None:
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        run_comms_test()
    except EOFError:
        sys.stderr.write("\n\nERROR: Communication stream interrupted.\n")
    except KeyboardInterrupt:
        sys.stderr.write("\n\nALERT: Connection terminated by operator.\n")


if __name__ == "__main__":
    main()
