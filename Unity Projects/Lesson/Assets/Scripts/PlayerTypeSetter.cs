using UnityEngine;
using UnityEngine.UI;

public class PlayerTypeSetter : MonoBehaviour
{

    public Toggle cube;
    public Toggle cylinder;
    public Toggle capsule;
    public Toggle sphere;

    private void Start()
    {
        switch (PlayerPrefs.GetString("Type", "Cube"))
        {
            case "Cube":
                cube.isOn = true;
                cylinder.isOn = false;
                capsule.isOn = false;
                sphere.isOn = false;
                break;
            case "Capsule":
                cube.isOn = false;
                cylinder.isOn = false;
                capsule.isOn = true;
                sphere.isOn = false;
                break;
            case "Sphere":
                cube.isOn = false;
                cylinder.isOn = false;
                capsule.isOn = false;
                sphere.isOn = true;
                break;
            case "Cylinder":
                cube.isOn = false;
                cylinder.isOn = true;
                capsule.isOn = false;
                sphere.isOn = false;
                break;
            default:
                break;
        }
    }

    public void Cube(bool value)
    {
        if (value)
        {
            PlayerPrefs.SetString("Type", "Cube");

            cube.isOn = value;
            cylinder.isOn = !value;
            capsule.isOn = !value;
            sphere.isOn = !value;
        }
    }

    public void Cylinder(bool value)
    {
        if (value)
        {
            PlayerPrefs.SetString("Type", "Cylinder");

            cube.isOn = !value;
            cylinder.isOn = value;
            capsule.isOn = !value;
            sphere.isOn = !value;
        }
    }

    public void Capsule(bool value)
    {
        if (value)
        {
            PlayerPrefs.SetString("Type", "Capsule");

            cube.isOn = !value;
            cylinder.isOn = !value;
            capsule.isOn = value;
            sphere.isOn = !value;
        }
    }

    public void Sphere(bool value)
    {
        if (value)
        {
            PlayerPrefs.SetString("Type", "Sphere");

            cube.isOn = !value;
            cylinder.isOn = !value;
            capsule.isOn = !value;
            sphere.isOn = value;
        }
    }
}
