type AudiobookProps = {
  id: string;
  title: string;
  author: string;
  coverImage: string;
  votes: number;
  onVote: (id: string) => void;
};

const AudiobookCard: React.FC<AudiobookProps> = ({
  id,
  title,
  author,
  coverImage,
  votes,
  onVote,
}) => {
  const handleVote = () => {
    onVote(id);
  };

  return (
    <div className="max-w-sm mx-auto bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div className="relative">
        <img className="w-full h-64 object-cover" src={coverImage} alt={title} />

        <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-70"></div>

        <div className="absolute bottom-4 left-4 text-white text-left">
          <h2 className="text-lg font-bold">{title}</h2>
          <p className="text-sm">{author}</p>
        </div>
      </div>

      <div className="p-4 bg-gradient-to-br from-blue-100 to-purple-100 rounded-b-xl">
        <div className="flex justify-between items-center">
          <span className="text-xl font-semibold text-gray-800">{votes} votes</span>

          <button
            onClick={handleVote}
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full transition-transform transform hover:scale-105"
          >
            Vote
          </button>
        </div>
      </div>
    </div>
  );
};

export default AudiobookCard;
