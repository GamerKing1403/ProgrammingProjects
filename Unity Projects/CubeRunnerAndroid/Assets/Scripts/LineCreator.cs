using UnityEngine;

public class LineCreator : MonoBehaviour
{
    public LineRenderer lineRenderer;
    private void Start()
    {
        Vector3 initialPosition = new Vector3(Screen.width/2,Screen.height,1);
        Vector3 finalPosition = new Vector3(Screen.width/2,0,1);
        lineRenderer.SetPosition(0, initialPosition);
        lineRenderer.SetPosition(1, finalPosition);
        lineRenderer.enabled = true;
    }
}
