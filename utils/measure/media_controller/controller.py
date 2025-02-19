from typing import Any, Protocol

import inquirer


class MediaController(Protocol):
    def set_volume(self, volume: int) -> None:
        ...

    def mute_volume(self) -> None:
        ...

    def play_audio(self, stream_url: str) -> None:
        ...

    def turn_off(self) -> None:
        ...

    def get_questions(self) -> list[inquirer.questions.Question]:
        ...

    def process_answers(self, answers: dict[str, Any]):
        ...
