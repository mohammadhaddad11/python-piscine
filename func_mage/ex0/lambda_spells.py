def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict[str, int | float]:
    if not mages:
        return {
            'max_power': 0,
            'min_power': 0,
            'avg_power': 0.0,
        }

    power_level = list(map(lambda m: m['power'], mages))

    return {
        'max_power': max(power_level),
        'min_power': min(power_level),
        'avg_power': round(sum(power_level) / len(power_level), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))
