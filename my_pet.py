# -*- coding: utf-8 -*-
"""终端版小宠物 —— ESP32 桌面宠物项目的第一个原型。

运行：
    python my_pet.py

输入：喂 / 玩 / 退出
"""

pet = {
    "name": "小豆",
    "mood": 50,     # 心情 0-100
    "hunger": 30,   # 饥饿 0-100，数字越大越饿
}


def draw_bar(value: int, width: int = 20) -> str:
    """把 0-100 的数值画成一条进度条。"""
    filled = int(value / 100 * width)
    return "█" * filled + "-" * (width - filled)


def show(pet: dict) -> None:
    print()
    print(f"  ┌─ {pet['name']} ─────────────")
    print(f"  │ 心情 {draw_bar(pet['mood'])} {pet['mood']:3d}")
    print(f"  │ 饥饿 {draw_bar(pet['hunger'])} {pet['hunger']:3d}")
    print(f"  └────────────────────────")


def feed(pet: dict) -> None:
    pet["hunger"] = max(0, pet["hunger"] - 20)
    pet["mood"] = min(100, pet["mood"] + 10)
    print("  你喂了它一口，它眯起了眼睛。")


def play(pet: dict) -> None:
    pet["mood"] = min(100, pet["mood"] + 15)
    pet["hunger"] = min(100, pet["hunger"] + 10)
    print("  你陪它玩了一会儿，它开心地转了个圈。")


def step(pet: dict) -> None:
    """过一回合：慢慢变饿，心情下滑。"""
    pet["hunger"] = min(100, pet["hunger"] + 8)
    pet["mood"] = max(0, pet["mood"] - 5)


def main() -> None:
    print("终端小宠物 v0.1   （输入：喂 / 玩 / 退出）")
    while True:
        show(pet)
        if pet["hunger"] >= 100:
            print("  它饿得趴下了……")
            break
        cmd = input("  > ").strip()
        if cmd in ("退出", "q", "exit"):
            print("  它目送你离开。")
            break
        elif cmd in ("喂", "feed"):
            feed(pet)
        elif cmd in ("玩", "play"):
            play(pet)
        else:
            print("  它歪了歪头，没听懂。")
        step(pet)


if __name__ == "__main__":
    main()
