# DO NOT MODIFY
import subprocess
import sys
import ast
import os
import tempfile


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def run_program(filename, inputs):
    """Runs a .py file with simulated stdin inputs."""
    process = subprocess.Popen(
        [sys.executable, filename],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input="\n".join(inputs))
    return stdout


def run_program_with_vars(filename, replacements):
    """
    Reads the .py file, replaces variable assignment lines
    according to replacements dict {"var": value}, and runs it.
    Example: replacements={"nums": [1,2,3]} replaces line 'nums = ...'
    """
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    lines = source.splitlines()
    new_lines = []
    for line in lines:
        replaced = False
        for var, value in replacements.items():
            if line.strip().startswith(f"{var} =") or line.strip().startswith(f"{var}="):
                new_lines.append(f"{var} = {repr(value)}")
                replaced = True
                break
        if not replaced:
            new_lines.append(line)

    modified_source = "\n".join(new_lines)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as tmp:
        tmp.write(modified_source)
        tmp_path = tmp.name

    try:
        process = subprocess.Popen(
            [sys.executable, tmp_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate()
    finally:
        os.unlink(tmp_path)

    return stdout


# ─────────────────────────────────────────────
# Question 1: Scholarship
# ─────────────────────────────────────────────

class TestScholarship:

    def test_bi_grants_scholarship_no_matter_what(self):
        output = run_program("beca.py", ["0.0", "0", "0", "1"])
        assert "True" in output

    def test_bi_grants_with_low_gpa(self):
        output = run_program("beca.py", ["2.0", "50", "200", "1"])
        assert "True" in output

    def test_meets_all_requirements(self):
        output = run_program("beca.py", ["3.5", "100", "260", "0"])
        assert "True" in output

    def test_exceeds_requirements(self):
        output = run_program("beca.py", ["4.5", "200", "350", "0"])
        assert "True" in output

    def test_insufficient_gpa(self):
        output = run_program("beca.py", ["3.4", "150", "300", "0"])
        assert "False" in output

    def test_zero_gpa(self):
        output = run_program("beca.py", ["0.0", "150", "300", "0"])
        assert "False" in output

    def test_insufficient_hours(self):
        output = run_program("beca.py", ["3.8", "99", "300", "0"])
        assert "False" in output

    def test_zero_hours(self):
        output = run_program("beca.py", ["3.8", "0", "300", "0"])
        assert "False" in output

    def test_insufficient_saber_pro(self):
        output = run_program("beca.py", ["3.8", "150", "259", "0"])
        assert "False" in output

    def test_zero_saber_pro(self):
        output = run_program("beca.py", ["3.8", "150", "0", "0"])
        assert "False" in output

    def test_fail_gpa_and_hours(self):
        output = run_program("beca.py", ["3.0", "80", "300", "0"])
        assert "False" in output

    def test_fail_everything(self):
        output = run_program("beca.py", ["1.0", "10", "100", "0"])
        assert "False" in output


# ─────────────────────────────────────────────
# Question 2: Finding the "s"
# ─────────────────────────────────────────────

class TestFindingS_Part1:

    def test_contains_lowercase_s(self):
        output = run_program("s_parte1.py", ["Estoy bajo demasiada presión"])
        assert "True" in output

    def test_does_not_contain_s(self):
        output = run_program("s_parte1.py", ["Voy a la reunión"])
        assert "False" in output

    def test_uppercase_S_in_sentence(self):
        output = run_program("s_parte1.py", ["Solo necesito un café"])
        assert "True" in output

    def test_only_uppercase_S(self):
        output = run_program("s_parte1.py", ["SALIDA"])
        assert "True" in output


# ─────────────────────────────────────────────
# Question 3: Unique Sums
# ─────────────────────────────────────────────

class TestUniqueSums:

    def test_positive_example(self):
        output = run_program_with_vars("sumas_unicas.py", {"nums": [0, 2, 4, 6]})
        result = sorted(ast.literal_eval(output.strip()))
        assert result == sorted([2, 4, 6, 8, 10])


# ─────────────────────────────────────────────
# Question 4: Engineering Calculations
# ─────────────────────────────────────────────

class TestValidTemp:

    def test_valid_input_direct(self):
        output = run_program("temp_valida.py", ["76"])
        assert "Valid input." in output

    def test_invalid_then_valid(self):
        output = run_program("temp_valida.py", ["hello", "76"])
        assert "Invalid input, try again." in output
        assert "Valid input." in output


class TestAverageSignals:

    def test_base_example(self):
        output = run_program_with_vars("promedio.py", {"signals": (3.3, 5.0, 4.2, 3.8)})
        assert float(output.strip()) == 4.075


class TestMaterialRecord:

    def test_steel_example(self):
        output = run_program_with_vars("registro_material.py", {"temp": 1200, "material": "Steel"})
        assert output.strip() == "Temperature recorded: 1200 degrees Celsius for material: Steel"