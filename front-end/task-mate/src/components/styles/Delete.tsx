import { Trash2Icon } from "lucide-react";
import axiosInstance from "../../api/axiosInstance";

interface DeleteProps {
  id: number;
  onDelete: (id: number) => void;
}

const Delete = ({ id, onDelete }: DeleteProps) => {

  const handleDelete = async () => {
    try {
      await axiosInstance.delete(`/to-do/update-task/${id}/`);
      onDelete(id); // 🔥 instantly updates UI
    } catch (error) {
      console.log("Delete error:", error);
    }
  };

  return (
    <Trash2Icon onClick={handleDelete} ></Trash2Icon>
  );
};

export default Delete;
