from vcfphasesets import read_vcf


def test_triploid():
    filename = "tests/data/test_triploid.vcf"
    sample_name, phase_sets = read_vcf(filename)

    assert sample_name == "example"

    assert phase_sets == {
        ("NG_008376.4", 5119): [[], [(5155, 5156, "TT")], [(5118, 5119, "T")]],
        ("NG_008376.4", 6755): [[(6754, 6755, "C")], [(6754, 6755, "C")], [(6754, 6755, "C")]],
        ("NG_008376.4", 7870): [[(8007, 8008, "A")], [(7869, 7870, "T"), (8007, 8008, "A")], [(7869, 7870, "T")]],
        ("NG_008376.4", 9200): [[], [], [(9199, 9200, "C")]],
    }
