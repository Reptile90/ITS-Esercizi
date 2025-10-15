import React, { useEffect, useState } from 'react'

const CheckboxMultipleConCounter = () => {
    const techSkills = [
        { id: 1, name: "JavaScript" },
        { id: 2, name: "React" },
        { id: 3, name: "Vue" },
        { id: 4, name: "Angular" },
        { id: 5, name: "TypeScript" },
        { id: 6, name: "Node.js" },
        { id: 7, name: "PHP" },
        { id: 8, name: "Laravel" },
        { id: 9, name: "WordPress" },
        { id: 10, name: "CSS/SASS" }
    ];

    const [selectedIds, setSelectedIds] = useState([]);

    const handleChange = (id) => {
        setSelectedIds((prev) =>
            prev.includes(id) ? prev.filter((item) => item != id) : [...prev, id]
        );
    };

    useEffect(() => {
        if (selectedIds.length > 5) {
            alert("Puoi selezionare al massimo 5 skills");
        }
    }, [selectedIds]);

    const handleReset = () => {
        setSelectedIds([]);
    };


 return (
    <div className="container mt-5">
      <div className="card shadow-sm">
        <div className="card-body">
          <h4 className="card-title mb-3">Checkbox Multiple con Counter</h4>

          <p
            className={`fw-bold ${selectedIds.length > 5 ? 'text-danger' : 'text-primary'}`}
          >
            Selezionate: {selectedIds.length} / {techSkills.length}
          </p>

          <div className="row">
            {techSkills.map((skill) => (
              <div className="col-6 col-md-4 mb-2" key={skill.id}>
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    id={`skill-${skill.id}`}
                    checked={selectedIds.includes(skill.id)}
                    onChange={() => handleChange(skill.id)}
                  />
                  <label
                    className={`form-check-label ${
                      selectedIds.includes(skill.id) ? 'fw-bold text-success' : ''
                    }`}
                    htmlFor={`skill-${skill.id}`}
                  >
                    {skill.name}
                  </label>
                </div>
              </div>
            ))}
          </div>

          <div className="mt-4">
            <h6>Skills selezionate:</h6>
            {selectedIds.length === 0 ? (
              <p className="text-muted">Nessuna selezione</p>
            ) : (
              <ul className="list-group">
                {selectedIds.map((id) => {
                  const skill = techSkills.find((s) => s.id === id);
                  return <li className="list-group-item" key={id}>{skill?.name}</li>;
                })}
              </ul>
            )}
          </div>

          <button className="btn btn-outline-secondary mt-3" onClick={handleReset}>
            Reset
          </button>
        </div>
      </div>
    </div>
  );
};


export default CheckboxMultipleConCounter